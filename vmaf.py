import asyncio
import shlex
import re

from util import load_config

pattern = r"VMAF score: ([\d.]+)"

def add_vmaf_subcommand(parsers):
    vmaf_parser = parsers.add_parser('vmaf', help='Run VMAF calculation')
    vmaf_parser.add_argument("--input1", type=str, default="/home/iuz/video/ff_dota_30_1080.mp4", help="input file path")
    vmaf_parser.add_argument("--input2", type=str, default="/home/iuz/video/dota_30_1080_hevc.mp4", help="input file path")
    vmaf_parser.add_argument("--start", type=int, default=0, help="from v frame")
    vmaf_parser.add_argument("--max", type=int, default=30, help="max v frames")
    vmaf_parser.add_argument("--auto", action="store_true", help="auto detect max v frames")
    vmaf_parser.add_argument("--index1", type=int, default=0, help="start index for input1")
    vmaf_parser.add_argument("--index2", type=int, default=0, help="start index for input2")

    vmaf_parser.set_defaults(handler=_handle_vmaf_default)

    return vmaf_parser

async def _handle_vmaf_default(args):
    cfg_module = load_config()
    cfg = cfg_module.Config

    if args.auto:
        return await _handle_auto(args)
    
    cmd = f'{cfg.vmaf_ffmpeg} -i {args.input1} -i {args.input2} -lavfi libvmaf="log_path=vmaf_log.json:log_fmt=json" -f null - -y'
    print(cmd)
    await _run_cmd("vmaf", f"{args.index1}_{args.index2}", cmd)
    
async def _handle_auto(args):
    for j in range(args.max):
        i = j + args.start
        await _handle_vmaf_index(args, i, i)

async def _handle_vmaf_index(args, index1, index2):
    output1 = f'/home/iuz/images/ff_{index1}.png'
    cmd1 = f'/home/iuz/ffmpeg/ffmpeg -i {args.input1} -vf "select=\'eq(n,{index1})\'" -vframes 1 {output1} -y'
    await _run_cmd("ff", index1, cmd1)
    output2 = f'/home/iuz/images/ni_{index2}.png'
    cmd2 = f'/home/iuz/ffmpeg/ffmpeg -i {args.input2} -vf "select=\'eq(n,{index2})\'" -vframes 1 {output2} -y'
    await _run_cmd("ni", index2, cmd2)
    cmd3 = f'/home/iuz/ffmpeg/ffmpeg -i {output1} -i {output2} -lavfi libvmaf="log_path=vmaf_ff_{index1}_{index2}.json:log_fmt=json" -f null - -y'
    await _run_cmd("vmaf", f"{index1}_{index2}", cmd3)

async def _run_cmd(name: str, msg: str, cmd: str):
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
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                text = line.decode(errors="ignore").strip()
                match = re.search(pattern, text)
                if match:
                    score = float(match.group(1))
                    print(f"[{prefix}] <{msg}> {score}")
    
    await asyncio.gather(
        read_stream(process.stdout, f"{name}-stdout"),
        read_stream(process.stderr, f"{name}-stderr"),
    )

    await process.wait()