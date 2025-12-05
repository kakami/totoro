import asyncio
import shlex
import re

pattern = r"speed=([\d.]+)"

async def run_ffmpeg(name: str, cmd: str, queue: asyncio.Queue):
    print(f"[{name}] start...")
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