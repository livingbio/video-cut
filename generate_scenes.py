#!/usr/bin/env python

import random
import copy
import logging
import sys

import cut


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_score(image, text):
    score = random.random()
    return score


def get_best_scene(scene_list, text):
    score_list = [get_score(scene['image'], text) for scene in scene_list]
    best_score = max(score_list)

    logger.debug(score_list)
    logger.debug(best_score)

    return copy.copy(scene_list[score_list.index(best_score)])


def generate_scenes(text_list, filename='default.mp4', threshold=0.6):
    """Return corresponding scenes from input text and video

    :param text_list: A list of text for scene generation
    :param filename: Video file
    :param threshold: A tunable threshold of scene cut

    :type text_list: list
    :type filename: str
    :type threshold: float

    :return: A dictionary for result scene generation and all scenes for the input video
    :rtype: dict
    """

    scene_list = cut.cut_scenes(filename, threshold)
    result = []

    for text in text_list:
        best_scene = get_best_scene(scene_list, text)
        best_scene['text'] = text
        result.append(best_scene)

    return {
        'result': result,
        'scene_list': scene_list,
    }
