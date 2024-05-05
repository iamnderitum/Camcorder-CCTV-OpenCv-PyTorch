import numpy as np
import cv2

def image_channels():
    image = cv2.imread("image.jpg")
    cv2.imshow("Image", image)
    cv2.moveWindow("Image", 0,0)
    print(image.shape)
    height, width, channels = image.shape

    # Split Channels of color image into its components in individual matrix
    b, g, r = cv2.split(image) 
    rgb_split = np.empty([height, width*3, 3], "uint8")

    rgb_split[:, 0:width] = cv2.merge([b,b,b])
    rgb_split[:, width:width*2] = cv2.merge([g,g,g])
    rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])
    cv2.imshow("Channels", rgb_split)
    cv2.moveWindow('Channels', 0, height)


    # HUE saturation value space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v =cv2.split(hsv)
    hsv_split = np.concatenate((h, s, v), axis=1)
    cv2.imshow("Split HSV",hsv_split)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

   


image_channels()