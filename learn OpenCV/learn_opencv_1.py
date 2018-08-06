import cv2
import pathlib
import matplotlib.pyplot as plt

basePath =  pathlib.Path.cwd()
# print(basePath)
fileName = basePath / 'learn OpenCV/media/smallbeach.jpg'
# print(type(fileName.resolve()))
# print(fileName.e1ists())
# img = cv2.imread("C:\\Users\\Jason\\Desktop\\machine learning ai\\learn OpenCV\\images\\smallbeach.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread(str(fileName), cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
