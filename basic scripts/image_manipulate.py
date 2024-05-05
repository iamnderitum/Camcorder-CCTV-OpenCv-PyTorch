import numpy as np
import cv2

def manipulate_image():
    img = cv2.imread("butterfly.jpg", 1)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("gray.jpg", gray)

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    rgba = cv2.merge((b, g, r, g)) # We are using the last g as the transparency layer
    cv2.imwrite("rgba.png", rgba)

manipulate_image()