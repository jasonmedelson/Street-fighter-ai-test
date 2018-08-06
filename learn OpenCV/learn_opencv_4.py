import cv2
import pathlib
import matplotlib.pyplot as plt

basePath =  pathlib.Path.cwd()
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
img = cv2.imread(str(fileName), cv2.IMREAD_COLOR)

px = img[55,55] #specific pixel color

#img[100:150,100:150] = [255,255,255]

location = img[125:175,125:175]
img[0:50,0:50] = location

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
