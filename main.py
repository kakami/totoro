# main.py

import argparse
import asyncio
import time
from vmaf import add_vmaf_subcommand
from transcode import add_transcode_subcommand
from util import ensure_config_exists

async def run():
    ensure_config_exists()
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='related commands')
    add_vmaf_subcommand(subparsers)
    add_transcode_subcommand(subparsers)
    args = parser.parse_args()

    if hasattr(args, "handler"):
        h = args.handler
        if asyncio.iscoroutinefunction(h):
            return await h(args)
        else:
            return h(args)
        
    parser.print_help()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())