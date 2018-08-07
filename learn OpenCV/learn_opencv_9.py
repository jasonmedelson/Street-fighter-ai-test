import cv2
import pathlib
import matplotlib.pyplot as plt
import numpy as np

basePath =  pathlib.Path.cwd()
fileName = basePath / 'learn OpenCV/media/drive.mp4'

cap = cv2.VideoCapture(str(fileName))

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110,70,50])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations = 1)
    # dilation = cv2.dilate(mask, kernel, iterations = 1)
    # opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)


    cv2.imshow('frame', closing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
