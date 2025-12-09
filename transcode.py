import asyncio
import time
import shlex
import re
from util import load_config
from template import ffmpeg_cmd

pattern = r"speed=([\d.]+)"
concurrency = 5

def add_transcode_subcommand(parsers):
    parser = parsers.add_parser('transcode', help='Run video transcoding')
    parser.add_argument("-c", "--concurrency", type=int, default=5, help="concurrency")
    parser.add_argument("-t", "--template", type=str, default="uhd60", help="template name")
    parser.add_argument("-l", "--list", action="store_true", help="list available templates")
    parser.add_argument("-C", "--command", action="store_true", help="print ffmpeg command only")

    parser.set_defaults(handler=_handle_transcode_default)
    return parser

async def _handle_transcode_default(args):
    cfg_module = load_config()
    cfg = cfg_module.Config
    concurrency = args.concurrency

    if args.list:
        from template import H264TEMPLATES, H265TEMPLATES
        print("H264 Templates:")
        print("  " + "/".join(H264TEMPLATES))
        print("H265 Templates:")
        print("  " + "/".join(H265TEMPLATES))
        return
    
    if args.command:
        print(ffmpeg_cmd(args.template, cfg.input, 0))
        return
    
    tasks = []
    queue = asyncio.Queue()
    stop_event = asyncio.Event()
    aggregator_task = asyncio.ensure_future(_speed_aggregator(queue, stop_event))
    for i in range(args.concurrency):
        t = asyncio.ensure_future(
            _run_ffmpeg(
                f"task{i+1}",
                ffmpeg_cmd(args.template, cfg.input, i),
                queue
            )
        )
        tasks.append(t)


    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        pass
    finally:
        stop_event.set()
        await aggregator_task

async def _speed_aggregator(queue: asyncio.Queue, stop_event: asyncio.Event):
    speeds = []
    last_report = time.time()
    print('--- Speed Aggregator Started ---')

    while not stop_event.is_set() or not queue.empty():
        try:
            # 最长等 0.1 秒，避免阻塞退出
            speed = await asyncio.wait_for(queue.get(), timeout=0.1)
            speeds.append(speed)
        except asyncio.TimeoutError:
            pass

        # 每秒打印一次
        if time.time() - last_report >= 1:
            if speeds:
                avg_speed = sum(speeds) / len(speeds)
                print(f"Concurrency: {concurrency}, Average speed: {round(avg_speed, 3)}")
                speeds.clear()
            last_report = time.time()

    print("Aggregator exit.")

async def _run_ffmpeg(name: str, cmd: str, queue: asyncio.Queue):
    print(f"[{name}] start...")
    print(f"[{cmd}]")
    process = await asyncio.create_subprocess_exec(
        *shlex.split(cmd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    async def read_stream(stream, prefix):
        buffer = b""
        while True:
            chunk = await stream.read(1024)
            if not chunk:
                break
            buffer += chunk
            while b"\r" in buffer:
                line, buffer = buffer.split(b"\r", 1)
                text = line.decode(errors="ignore").strip()
                match = re.search(pattern, text)
                if match:
                    speed = float(match.group(1))
                    # print(f"[{prefix}] {speed}")
                    await queue.put(speed)
    
    await asyncio.gather(
        read_stream(process.stdout, f"{name}-stdout"),
        read_stream(process.stderr, f"{name}-stderr"),
    )

    return_code = await process.wait()
    print(f"[{name}] finished with return code {return_code}")
    return return_code