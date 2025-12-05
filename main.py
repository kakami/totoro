# main.py

import argparse
import asyncio
import time
from run import run_ffmpeg
from template import ffmpeg_cmd

async def speed_aggregator(queue: asyncio.Queue, stop_event: asyncio.Event):
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
                print("Average speed:", round(avg_speed, 3))
                speeds.clear()
            last_report = time.time()

    print("Aggregator exit.")

async def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int, default=5, help="concurrency")
    parser.add_argument("-t", "--template", type=str, default="uhd60", help="template name")
    parser.add_argument("-l", "--list", action="store_true", help="list available templates")
    parser.add_argument("-C", "--command", action="store_true", help="print ffmpeg command only")
    parser.add_argument("--input", type=str, default="/home/iuz/video/dota_60_1080.mp4", help="input file path")
    args = parser.parse_args()

    input = args.input
    if args.list:
        from template import H264TEMPLATES, H265TEMPLATES
        print("H264 Templates:")
        print("  " + "/".join(H264TEMPLATES))
        print("H265 Templates:")
        print("  " + "/".join(H265TEMPLATES))
        return

    if args.command:
        print(ffmpeg_cmd(args.template, input, 0))
        return

    tasks = []
    queue = asyncio.Queue()
    stop_event = asyncio.Event()
    aggregator_task = asyncio.ensure_future(speed_aggregator(queue, stop_event))
    for i in range(args.concurrency):
        t = asyncio.ensure_future(
            run_ffmpeg(
                f"task{i+1}",
                ffmpeg_cmd(args.template, input, i),
                queue
            )
        )
        tasks.append(t)


    # results = await asyncio.gather(*tasks)
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        pass
    finally:
        stop_event.set()
        # for t in tasks:
            # t.cancel()
        await aggregator_task
    # print("All tasks completed:", results)

if __name__ == "__main__":
    # main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())