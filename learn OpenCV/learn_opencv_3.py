import cv2
import pathlib
import matplotlib.pyplot as plt

basePath =  pathlib.Path.cwd()
# print(basePath)
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
# print(type(fileName.resolve()))
# print(fileName.e1ists())
# img = cv2.imread("C:\\Users\\Jason\\Desktop\\machine learning ai\\learn OpenCV\\images\\smallbeach.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread(str(fileName), cv2.IMREAD_COLOR)

cv2.line(img, (0,0),(150,150),(255,255,255), 10) # (img, cords1,cords2,color BGR, line width)
cv2.rectangle(img, (15,15),(100,100), (255,0,0), 10) #(img,cords1,cords2,color BGR, line width)
cv2.circle(img, (100,100), 50, (0,0,255),10) #(img,center,radius,color BGR, line width)
#cv2.polygon() for any other shape

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Text',(0,130),font,1,(0,255,0),2,cv2.LINE_AA) #(img,text,start point, font, font size, font color, thickness, line)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
