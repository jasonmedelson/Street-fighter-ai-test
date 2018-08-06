import cv2
import pathlib
import matplotlib.pyplot as plt
import numpy as np

basePath =  pathlib.Path.cwd()
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
img = cv2.imread(str(fileName), cv2.IMREAD_GRAYSCALE)
retval, threshold = cv2.threshold(img, 50, 155, cv2.THRESH_BINARY )

gaus = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)

cv2.imshow('image', img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
