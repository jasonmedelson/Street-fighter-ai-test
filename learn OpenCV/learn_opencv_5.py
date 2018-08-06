import cv2
import pathlib
import matplotlib.pyplot as plt

basePath =  pathlib.Path.cwd()
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
img1 = cv2.imread(str(fileName), cv2.IMREAD_COLOR)
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
img2 = cv2.imread(str(fileName), cv2.IMREAD_GRAYSCALE)

# add = img1 + img2 # no oppacity
# add = cv2.add(img1,img2) # adds colors, if over 255 set to 255
# weighted = cv2.addWeighted(img1,0.6,img2,0.4,0) #with oppacity changed

# rows,cols,channels = img2.shape
# roi = img1[0:rows,0:cols]




cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
