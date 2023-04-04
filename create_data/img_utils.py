import matplotlib.pyplot as plt
from create_data.modify_img import *
from spot_difference.spot_diff import *


def show_two_img(img1, img2, title1="Original Image", title2=None):
    '''
    Show to image side by side
    :param img1: 1st image
    :param img2: 2nd image
    :param title1: title of 1st image
    :param title2: title of 2nd image
    :return: None
    '''
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    ax1.imshow(img1[:, :, ::-1])
    ax1.set_title(title1)
    ax1.axis('off')
    ax2.imshow(img2[:, :, ::-1])
    ax2.set_title(title2)
    ax2.axis('off')

    plt.show()


def show_level(img, level=1, spot_diff=False):
    '''
    Show the original image and the modified image of the level
    :param img: input image
    :param level: game level (1->5)
    :return: None
    '''
    level_img = []
    plt.rcParams['figure.figsize'] = [12, 8]
    if level == 1:
        level_img = draw_random_rectangle(img, LEVEL1)
    elif level == 2:
        level_img = draw_avg_rectangle(img, LEVEL2)
    elif level == 3:
        level_img = flip_rectangle(img, LEVEL3)
    elif level == 4:
        level_img = change_edge_color(img, LEVEL4)
    elif level == 5:
        level_img = change_object_color(img, LEVEL5)

    if spot_diff:
        level_img = spot_the_difference(img, level_img)

    show_two_img(img, level_img, title2="Level %s" % level)
