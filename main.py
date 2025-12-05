# main.py

import argparse
import asyncio
from time import time
from template import build_ffmpeg_cmd
from run import run_ffmpeg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    cmd = build_ffmpeg_cmd(args.template, args.input, args.output)
    print(cmd)

async def speed_aggregator(queue: asyncio.Queue, stop_event: asyncio.Event):
    speeds = []
    last_report = time.time()

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
                print("Average speed:", round(avg_speed, 3))
            last_report = time.time()

    print("Aggregator exit.")

async def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int, default=5, help="concurrency")
    args = parser.parse_args()

    tasks = []
    queue = asyncio.Queue()
    stop_event = asyncio.Event()
    aggregator_task = asyncio.ensure_future(speed_aggregator(queue, stop_event))
    for i in range(args.concurrency):
        tasks.append(
            run_ffmpeg(
                f"task{i+1}",
                f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 0 -xcoder-params "out=hw:enableOut1=1:scale1=0x720" -y -vsync 0 -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -c:v h265_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=3500000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/video/out{i+1}.mp4',
                queue
            )
        )


    results = await asyncio.gather(*tasks)
    stop_event.set()
    await aggregator_task
    print("All tasks completed:", results)

if __name__ == "__main__":
    # main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())