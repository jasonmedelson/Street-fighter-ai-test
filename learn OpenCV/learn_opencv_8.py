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

    # kernal = np.ones((15,15), np.float32)/255
    # smoothed = cv2.filter2D(res,-1,kernal)

    # blur = cv2.GaussianBlur(res,(15,15), 0)
    # median = cv2.medianBlur(res,15)
    # bilateral = cv2.bilateralFilter(res,15,75,75)



    cv2.imshow('frame', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
