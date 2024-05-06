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

#manipulate_image()
image = cv2.imread("logo.jpg", 1)
def image_resize():
    #image = cv2.imread("logo.jpg", 1)

    #SCALE
    image_half = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
    image_stretch = cv2.resize(image, (600,600))
    image_stretch_near = cv2.resize(image, (600, 600), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("Half", image_half)
    cv2.imshow("stretch", image_stretch)
    cv2.imshow("Stretch near", image_stretch_near)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#image_resize()

def image_rotation():
    M = cv2.getRotationMatrix2D((0, 0), -30, 1)
    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[1]))
    cv2.imshow("Rotated", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_rotation()