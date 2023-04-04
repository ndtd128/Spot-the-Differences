import cv2 as cv
import matplotlib.pyplot as plt
from create_data.img_utils import *
from create_data.modify_img import *


def main():
    img = cv.imread("images/bar.jpg")
    show_level(img, 5, spot_diff=True)


if __name__ == "__main__":
    main()
