#capture from video file

import cv2
import pathlib
import matplotlib.pyplot as plt

basePath =  pathlib.Path.cwd()
# print(basePath)
fileName = basePath / 'learn OpenCV/media/drive.mp4'
print(fileName.exists())

cap = cv2.VideoCapture(str(fileName))

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    reverse= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',frame)
    cv2.imshow('grey',gray)
    cv2.imshow('reversed',reverse)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
