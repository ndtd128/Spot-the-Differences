import random
from create_data.constant import *
import cv2 as cv


def generate_rects(img, num_of_rects, min_h=MIN_H, max_h=MAX_H, min_w=MIN_W, max_w=MAX_W):
    '''
    This function generate random rectangles
    :param img: input image
    :param num_of_rects: how many rects to generate
    :param min_h: minimum height of rect
    :param max_h: maximum height of rect
    :param min_w: minimum width of rect
    :param max_w: maximum width of rect
    :return: a list of random rects
    '''
    rects = []
    shape = img.shape
    height, width = shape[0], shape[1]
    while len(rects) < num_of_rects:
        x = random.randint(0, width - max_w)
        y = random.randint(0, height - max_h)
        w = random.randint(min_w, max_w)
        h = random.randint(min_h, max_h)

        if not overlap_rect(x, y, w, h, rects):
            rects.append((x, y, x + w, y + h))

    return rects


def overlap_rect(x, y, w, h, rects):
    '''
    Check if the input (x, y, w, h) are overlap with rect in rects
    :param x: x-coordinate
    :param y: y coordinate
    :param w: width of the rect
    :param h: height of the rect
    :param rects: a list of rectangle
    :return: if the new rect are not overlap with any rect in rects, return False
    '''
    if len(rects) == 0:
        return False
    for rect in rects:
        if (x + w < rect[0] or y + h < rect[1]
                or rect[2] < x or rect[3] < y):
            return False

    return True


def generate_color():
    '''
    Generate random RGB color
    :return: a tuple of (red, green, blue) value
    '''
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return r, g, b
    # return (255, 0, 0)
