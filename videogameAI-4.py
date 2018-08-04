import numpy as np
from PIL import ImageGrab
import cv2
import time

def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img,(coords[0],coords[1]), (coords[2],coords[3]), [255,255,255],2) #(img, (x1,y1),(x2,y2), color of line, line thickness)
    except:
        pass


def process_img(original_image):
##    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(original_image, threshold1=100, threshold2=300)
    cv2.GaussianBlur(processed_img, (5,5),0)
    lines = cv2.HoughLinesP(processed_img, 1 ,np.pi/180, 100, 5, 5) #(image, 1, np.pi/180, 100, min line length, line gap fill)
    draw_lines(processed_img,lines)


    return processed_img
window_name = "StreetFighterV"
cv2.namedWindow( window_name, cv2.WINDOW_AUTOSIZE )
last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,1400,800)))
    new_screen = process_img(screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow(window_name, new_screen)
##    cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
