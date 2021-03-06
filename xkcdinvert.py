# This program inverts xkcd comic images by swapping around the s and v values in HSV color space.

# By Kwonunn 2020

import numpy as np
import imageio
from PIL import Image
import colorsys
import sys

def toFloat(i):
    return i / 0xFF


def to255(i):
    return i * 0xFF


def main():
    if (sys.argv.__len__() > 1):
        uri = sys.argv[1]
    else:
        uri = "xkcd.png"
        
    image = Image.open(uri).convert("RGB")
    nparray = np.array(image)
    array = nparray.tolist()
    del nparray

    try:
        array[0][0][0]
    except TypeError:
        for col in range(array.__len__()):
            for p in range(array[col].__len__()):
                array[col][p] = 0xFF - array[col][p]
    else:
        for col in array:
            for p in col:
                if (p[0] == p[1] == p[2]):
                    p[0] = 0xFF - p[0]
                    p[1] = 0xFF - p[1]
                    p[2] = 0xFF - p[2]
                else:
                    hsv = colorsys.rgb_to_hsv(
                        toFloat(p[0]), toFloat(p[1]), toFloat(p[2]))
                    rgb = colorsys.hsv_to_rgb(hsv[0], hsv[2], hsv[1])
                    p[0] = to255(rgb[0])
                    p[1] = to255(rgb[1])
                    p[2] = to255(rgb[2])

    imageio.imsave("xkcdinverted.png", array)


if __name__ == "__main__":
    main()
