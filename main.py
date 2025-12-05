# main.py

import argparse
import asyncio
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

async def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int, default=2, help="concurrency")
    args = parser.parse_args()

    tasks = []
    global_speeds = []
    for i in range(args.concurrency):
        tasks.append(
            run_ffmpeg(
                f"task{i+1}",
                f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 0 -xcoder-params "out=hw:enableOut1=1:scale1=0x720" -y -vsync 0 -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -c:v h265_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=3500000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/video/out{i+1}.mp4',
                global_speeds
            )
        )


    results = await asyncio.gather(*tasks)
    print("All tasks completed:", results)

if __name__ == "__main__":
    # main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())