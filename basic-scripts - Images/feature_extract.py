### BINARY IMAGE SEGMENTATION
import numpy as np
import cv2

bw = cv2.imread("images/detect_blob.jpg", 0)
#bw = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(bw.shape)


# 1. Simple Thresholding
def simple_thresholding():
    height, width = bw.shape[0: 2]
    cv2.imshow("Original BW", bw)

    binary = np.zeros([height, width, 1], "uint8")

    thresh = 185

    for row in range(0, height):
        for col in range(0, width):
            if bw[row][col] > thresh:
                binary[row][col] = 255

    cv2.imshow("Slow Binary", binary)

    ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY )
    cv2.imshow("CV Threshold", thresh)
    

#simple_thresholding()

# 2. ADAPTIVE Thresholding
def adaptive_threshold():
    cv2.imshow("Original BW", bw)
    thresh_adapt = cv2.adaptiveThreshold(bw, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,115, 1)
    cv2.imshow("CV Threshold", thresh_adapt)

adaptive_threshold()

cv2.waitKey(0)
cv2.destroyAllWindows()