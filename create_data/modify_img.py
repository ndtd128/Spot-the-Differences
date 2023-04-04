import random

import cv2 as cv
import numpy as np
from create_data.utils import *
from create_data.constant import *


def draw_random_rectangle(img, num_changes):
    '''
    Draw ramdom rects into the input image with random color
    :param img: input image
    :param num_changes: number of rects to draw
    :return: a modified image
    '''
    copy_img = img.copy()
    rects = generate_rects(img, num_changes)

    # draw rect to img
    for rect in rects:
        # random color
        color = generate_color()

        cv.rectangle(copy_img, (rect[0], rect[1]), (rect[2], rect[3]), color[::-1], cv.FILLED)

    return copy_img


def draw_avg_rectangle(img, num_changes):
    '''
    Draw ramdom rects into the input image with the average color of the area
    :param img: input image
    :param num_changes: number of rects to draw
    :return: a modified image
    '''
    copy_img = img.copy()
    rects = generate_rects(img, num_changes)

    # draw rect to img
    for rect in rects:
        # get the avg color of the area
        xA, yA = rect[0], rect[1]
        xB, yB = rect[2], rect[3]
        avg_color_row = np.average(img[yA:yB, xA:xB], axis=0)
        avg_color = np.average(avg_color_row, axis=0)

        cv.rectangle(copy_img, (xA, yA), (xB, yB), avg_color, cv.FILLED)

    return copy_img


def flip_rectangle(img, num_changes):
    '''
    Flip some area by vertically or horizontally or both
    :param img: input image
    :param num_changes: number of areas to flip
    :return: a modified image
    '''
    copy_img = img.copy()
    rects = generate_rects(img, num_changes)

    # draw rect to img
    for rect in rects:
        # area to flip
        xA, yA = rect[0], rect[1]
        xB, yB = rect[2], rect[3]
        area = img[yA:yB, xA:xB]

        choices = [1, 0, -1]
        # 1: flip horizontally
        # 0: flip vertically
        # -1: flip both horizontally and vertically

        flip_direction = random.choice(choices)
        copy_img[yA:yB, xA:xB] = cv.flip(area, flip_direction)

    return copy_img


def _find_contours(img, min_area, max_area):
    '''
    find the contour of the image, filter it by contour's area
    :param img: input image
    :param min_area: minimum contour's area
    :param max_area: maximum contour's area
    :return: a list of filtered contours
    '''
    copy_img = img.copy()

    gray_img = cv.cvtColor(copy_img, cv.COLOR_BGR2GRAY)

    # Detect edges with Canny
    canny_img = cv.Canny(gray_img, 30, 250)

    contours, hierarchy = cv.findContours(canny_img.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    filtered_contours = []
    for contour in contours:
        if min_area < cv.contourArea(contour) < max_area:
            filtered_contours.append(contour)

    return filtered_contours


def change_edge_color(img, num_changes):
    '''
    Change random edge's color
    :param img: input image
    :param num_changes: number of edges to change color
    :return: a modified image
    '''
    copy_img = img.copy()
    contours = _find_contours(copy_img, MIN_AREA, MAX_AREA)

    # Choose random contours to change
    if len(contours) <= num_changes:
        selected = list(range(len(contours)))
    else:
        selected = random.sample(range(len(contours)), num_changes)

    print(len(selected))

    for i in range(len(selected)):
        # random color
        color = generate_color()

        cv.drawContours(copy_img, contours, selected[i], color[::-1], 2)

    return copy_img


def change_object_color(img, num_changes):
    '''
    Change the color of an object (area) in the image
    :param img: input image
    :param num_changes: number of areas to change
    :return: a modified image
    '''
    copy_img = img.copy()
    contours = _find_contours(copy_img, MIN_POLY_AREA, MAX_POLY_AREA)

    # Choose random contours to change
    if len(contours) <= num_changes:
        selected = list(range(len(contours)))
    else:
        selected = random.sample(range(len(contours)), num_changes)

    print(len(selected))

    for i in range(len(selected)):
        # random color
        color = generate_color()

        # area = [contours[selected[i]]]
        cv.fillPoly(copy_img, [contours[selected[i]]], color[::-1])

    return copy_img

