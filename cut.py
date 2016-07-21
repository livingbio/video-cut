#!/usr/bin/env python

import re
import subprocess
import logging
import sys
from os.path import basename


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def cut_scenes(filename='default.mp4', threshold=0.6):
    command = [
        "ffmpeg",
        "-i", filename,
        "-filter", "select='gt(scene,{0})',showinfo".format(threshold),
        "-vsync", "0",
        "frames/{0}.%06d.jpg".format(basename(filename)),
    ]
    logger.info("Begin of running ffmpeg")

    proc = subprocess.Popen(
        command, stdin=subprocess.PIPE, stderr=subprocess.PIPE
    )
    proc.wait()
    if proc.returncode:
        logger.error("There are some error in ffmpeg.")
        logger.error(proc.communicate()[1])
        return []

    pattern = re.compile(r"pts_time:(?P<pts_time>\d+.\d+)")
    scene_list = []
    last_timestamp = 0.0

    for line in proc.communicate()[1].split('\n'):
        match = pattern.search(line)
        if match:
            timestamp = float(match.groups()[0])
            scene_info = {
                'from_ts': last_timestamp,
                'to_ts': timestamp,
                'image': "frames/{0}.{1}.jpg".format(
                    basename(filename),
                    str(len(scene_list) + 1).zfill(6)
                ),
                'duration': timestamp - last_timestamp
            }
            scene_list.append(scene_info)
            last_timestamp = timestamp
            logger.info("Timestamp: %s", timestamp)

    logger.info("End of running ffmpeg")
    logger.debug(scene_list)

    return scene_list


if __name__ == "__main__":
    print(cut_scenes())
