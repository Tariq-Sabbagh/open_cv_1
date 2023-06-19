import cv2
import numpy as np
import cvzone
from cvzone.ColorModule import ColorFinder

ColorFinder(True)
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameWidth, frameHeight, _ = frame.shape

    centr_x = int(frameWidth / 2)
    centr_y = int(frameHeight / 2)

    pixle_center = HSV_frame[centr_y, centr_x]
    color_h = pixle_center[0]
    color = "White"

    if 170 < color_h < 180:
        color = "Red"
    elif color_h > 110 and color_h < 120:
        color = "Black"
    elif color_h > 10 and color_h < 30:
        color = "orange"
    elif color_h > 60 and color_h < 70:
        color = "Green"
    elif color_h > 90 and color_h < 105:
        color = "Blue"

    pixle_center_bgr = frame[centr_y, centr_x]
    r, g, b = pixle_center_bgr.tolist()

    cv2.putText(frame, color, (40, 110), 0, 4, (b, g, r), 9)

    print(pixle_center)
    cv2.circle(frame, (centr_x, centr_y), 100, (255, 255, 0), 4)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cap.destroyAllWindows()
