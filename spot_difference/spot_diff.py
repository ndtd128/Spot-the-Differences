import cv2 as cv
from create_data.constant import *

def spot_the_difference(original_img, modified_img):
    original_img_gray = cv.cvtColor(original_img, cv.COLOR_BGR2GRAY)
    modified_img_gray = cv.cvtColor(modified_img, cv.COLOR_BGR2GRAY)

    # Calc the difference
    diff = cv.absdiff(original_img_gray, modified_img_gray)

    # thresh to binary image
    thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Dilate to reduce small noise
    kernel = cv.getStructuringElement(cv.MORPH_DILATE, (5, 5))
    dilate_img = cv.dilate(diff, kernel, iterations=2)

    # Find contour of the differences
    contours, hierarchy = cv.findContours(dilate_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw bounder around the contours
    for contour in contours:
        if cv.contourArea(contour) > MIN_DIFF_AREA:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(modified_img, (x, y), (x + w, y + h), SPOT_COLOR[::-1], 3)

    return modified_img

