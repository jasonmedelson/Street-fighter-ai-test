import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_img(original_image):
##    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(original_image, threshold1=100, threshold2=300)
    return processed_img

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,1400,800)))
    new_screen = process_img(screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    # cv2.imshow('window',screen)
##    cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
