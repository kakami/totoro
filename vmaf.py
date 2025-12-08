import asyncio
import shlex
import re

pattern = r"VMAF score: ([\d.]+)"

def add_vmaf_subcommand(parsers):
    vmaf_parser = parsers.add_parser('vmaf', help='Run VMAF calculation')
    vmaf_parser.add_argument("--input1", type=str, default="/home/iuz/video/ff_dota_30_1080.mp4", help="input file path")
    vmaf_parser.add_argument("--input2", type=str, default="/home/iuz/video/dota_30_1080_hevc.mp4", help="input file path")
    vmaf_parser.add_argument("--start", type=int, default=0, help="from v frame")
    vmaf_parser.add_argument("--max", type=int, default=30, help="max v frames")

    vmaf_parser.set_defaults(handler=_handle_vmaf_default)

    return vmaf_parser

async def _handle_vmaf_default(args):
    for j in range(args.max):
        i = j + args.start
        output1 = f'ff_{i}.png'
        cmd1 = f'/home/iuz/ffmpeg/ffmpeg -i {args.input1} -vf "select=\'eq(n,{i})\'" -vframes 1 {output1} -y'
        await _run_cmd("ff", cmd1)
        output2 = f'ni_{i}.png'
        cmd2 = f'/home/iuz/ffmpeg/ffmpeg -i {args.input2} -vf "select=\'eq(n,{i})\'" -vframes 1 {output2} -y'
        await _run_cmd("ni", cmd2)
        cmd3 = f'/home/iuz/ffmpeg/ffmpeg -i {output1} -i {output2} -lavfi libvmaf="log_path=vmaf_ff.json:log_fmt=json" -f null - -y'
        await _run_cmd("vmaf", cmd3)

async def _run_cmd(name: str, cmd: str):
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
                    score = float(match.group(1))
                    print(f"[{prefix}] {score}")
    
    await asyncio.gather(
        read_stream(process.stdout, f"{name}-stdout"),
        read_stream(process.stderr, f"{name}-stderr"),
    )

    return_code = await process.wait()
    print(f"[{name}] finished with return code {return_code}")