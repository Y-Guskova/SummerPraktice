import cv2
import numpy as np

lower = np.array([100, 150, 20]) # set colour
upper = np.array([130, 255, 255])

video = cv2.VideoCapture(0)

while True:
    success, img = video.read() 

    if success: 

        if success:   
            
            image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(image, lower, upper)
    
    cv2.imshow('webcam', img)  
    cv2.imshow('mask', mask)

    cv2.waitKey(1)
