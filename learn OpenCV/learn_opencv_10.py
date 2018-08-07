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
    # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # sobelx = cv2.Sobel(frame, cv2.CV_64F, 1,0, ksize=5) #apply grayscale first
    # sobelx = cv2.Sobel(frame, cv2.CV_64F, 0,1, ksize=5) #apply grayscale first
    edges = cv2.Canny(frame, 200,250, 20)

    cv2.imshow('frame', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
