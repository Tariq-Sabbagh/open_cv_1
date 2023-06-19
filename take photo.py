import cv2
import numpy as np
import cvzone
img =cv2.VideoCapture(0)
while True:
    _,frame=img.read()
    cv2.imwrite("green.png",frame)
    cv2.waitKey(0)

