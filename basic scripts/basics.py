import numpy as np
import cv2

# Function to Access and Display Pixel Data
def display_image_features():
    img = cv2.imread("logo.jpg")
    #cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    #cv2.imshow("Image", img)

    #cv2.waitKey(0)

    #print(img)
    print("Image Type: ",type(img))
    print("\n Image Length: ",len(img[0]))
    print("\Image Length: ",len(img[0][0]))
    print("\nImage Shape: ",img.shape)
    print("\nImage Datatype: ",img.dtype)
    print("\nImage Size: ",img.size)

display_image_features()

## Data Tyoes and Structures
def image_dtypes_structures():
    black = np.zeros([150, 200, 1], "uint8") ## Create a black image
    cv2.imshow("Black", black)
    print(black[0,0,:])

    ones = np.ones([200, 150, 3], "uint8")
    cv2.imshow("Ones", ones)
    print(ones[0,0,:])

    white = np.ones([150, 200, 3], "uint16") ## Create white image
    white *= (2**16 - 1)
    cv2.imshow("White", white)
    print(white[0,0,:])

    color = ones.copy()
    color[:,:] = (255, 0, 0)
    cv2.imshow("Blue", color)
    print(color[0, 0, :])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_dtypes_structures()

