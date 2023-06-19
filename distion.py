import cv2
import numpy as np

# from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3, 420)
cap.set(4, 680)
while True:
    # Take each frame
    ret, frame = cap.read()
    if ret:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([140, 160, 100])
        upper_blue = np.array([150, 170, 110])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
