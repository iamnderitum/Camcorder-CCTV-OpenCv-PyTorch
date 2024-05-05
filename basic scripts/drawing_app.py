import numpy as np
import cv2

#GLOBAL VARIABLES
canvas = np.ones([500, 500, 3], "uint8")*255
color = (0, 255, 0)
radius = 3
pressed = False
# CLICK CALLBACK
def click(event, x, y, flags, param):
    global canvas, pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x,y), radius, color, -1)
        #print("LBUTTON Down")

    elif event == cv2.EVENT_MOUSEMOVE and pressed==True:
        cv2.circle(canvas, (x,y), radius, color, -1)
        #print("Mouse Move")

    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False
        #print("LButton Up")

## WINDOW INITIALIZATION & CALLBACK ASSIGNMENT
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever Draw loop

while True:

    cv2.imshow("canvas", canvas)

    #Key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord("q"):
        break

    elif ch & 0xFF == ord("b"):
        color = (255,0, 0)

    elif ch & 0xFF ==ord("g"):
        color = (0, 255, 0)

cv2.destroyAllWindows()