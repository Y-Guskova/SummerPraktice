import cv2
import numpy as np
def mask(lower, upper):
    video = cv2.VideoCapture(0)
    color_yellow= (0,255,255)
    while True:
        success, img = video.read() 

        if success: 

            if success:   
                
                image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(image, lower, upper)
        
         
        #cv2.imshow('mask', mask)

        moments = cv2.moments(mask, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0,0,255), -1)
            cv2.putText(img, "%d-%d" % (x,y), (x+10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
            print(x, y)
        file = open("otus.txt", "w")
        file.write(str(x) + '\n' + str(y)) 
        #file.write(str(y))
        file.close()
        cv2.imshow('webcam', img) 
        
        #cv2.waitKey(1)
        ch = cv2.waitKey(0)

        if ch == ord('q'):
         break

        

lower = np.array([100, 150, 20]) # set colour
upper = np.array([130, 255, 255])
mask(lower, upper)
