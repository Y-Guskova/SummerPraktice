#from turtle import ycor
import numpy as np
import cv2
import math

webcam = cv2.VideoCapture(0)

def find_cor():
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 0), 1)
                    rect = cv2.minAreaRect(contour)
                    center = (int(rect[0][0]), int(rect[0][1]))
                    cv2.circle(imageFrame, center, 2, (0, 0, 0), 2)
                    text = "(" + str(center[0]) + ", " + str(center[1]) + ")"
                   # cv2.putText(imageFrame, text, (center[0] + 10, center[1] + 10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 1, 8, 0)
                   # cv2.circle(imageFrame, (x, y), 0, (0,0,255), 0)
                    cv2.putText(imageFrame, "%d-%d" % (x,y), (x+10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,  (0, 0, 255), 1)

def gomografia(x,y):
  pts_img = np.array([[210, 115], [364, 111], [396,251], [186,248]])
  pts_real = np.array([[102, 53], [149, 57], [150, 112], [98,105]])

  h , status = cv2.findHomography(pts_img, pts_real)

  a = np.array([[x, y]], dtype='float32')
  a = np.array([a])

  points_out = cv2.perspectiveTransform(a, h)

  print (points_out)
  return points_out

deltax0_x1=500
deltay0_y1=500

deltax0_x2=500
deltay0_y2=500

#deltax0_x3=500
#deltay0_y3=500

deltax0_x4=500
deltay0_y4=500 

deltax0_x5=500
deltay0_y5=500

while(1):
  
  _, imageFrame = webcam.read()
  hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)



  # Green color and mask
  green_lower = np.array([40, 25, 150], np.uint8)
  green_upper = np.array([75, 255, 255], np.uint8)
  green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

  #Blue color and mask
  blue_lower = np.array([80, 50, 150], np.uint8)
  blue_upper = np.array([120, 255, 255], np.uint8)
  blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

  #Yellow color and mask
  yellow_lower = np.array([30, 50, 150], np.uint8)
  yellow_upper = np.array([35, 255, 255], np.uint8)
  yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)


  #Orange color and mask
  orange_lower = np.array([10, 50, 150], np.uint8)
  orange_upper = np.array([30, 255, 255], np.uint8)
  orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

  #Purple color and mask
  purple_lower = np.array([135, 50, 150], np.uint8)
  purple_upper = np.array([145, 255, 255], np.uint8)
  purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)
  
  kernal = np.ones((5, 5), "uint8")
  
  
  # For green color
  green_mask = cv2.dilate(green_mask, kernal)
  res_green = cv2.bitwise_and(imageFrame, imageFrame, mask = green_mask)
  
  # For blue color
  blue_mask = cv2.dilate(blue_mask, kernal)
  res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask = blue_mask)

  # For yellow color
  yellow_mask = cv2.dilate(yellow_mask, kernal)
  res_yellow = cv2.bitwise_and(imageFrame, imageFrame, mask = yellow_mask)

  # For orange color
  orange_mask = cv2.dilate(orange_mask, kernal)
  res_orange = cv2.bitwise_and(imageFrame, imageFrame, mask = orange_mask)

  # For purple color
  purple_mask = cv2.dilate(purple_mask, kernal)
  res_purple = cv2.bitwise_and(imageFrame, imageFrame, mask = purple_mask)
        

 #Contour for green color
  contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      #cv2.putText(imageFrame, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

#Detect coord green
  if len(contours) != 0:
    for contour in contours:
       area = cv2.contourArea(contour)
       if area > 500:
          find_cor()
          file = open("otus.txt", "w")
          file.write('1 ' +  str(x) + ' ' + str(y)  + '\n')  
          file.close()
          x1=x
          y1=y

  # Contour for blue color
  contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),(255, 0, 0), 2)  
      #cv2.putText(imageFrame, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

#Detect coord blue
  if len(contours) != 0:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            find_cor()
            file = open("otus.txt", "a+")
            file.write('2 ' +  str(x) + ' ' + str(y)  + '\n')  
            file.close()
            x2=x
            y2=y

# Contour for yellow color
  contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      #cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))  

#Detect coord yellow
  if len(contours) != 0:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            find_cor()
            file = open("otus.txt", "a+")
            file.write('3 ' +  str(x) + ' ' + str(y)  + '\n')  
            file.close()
            x3=x
            y3=y

# Contour for orange color
  contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      #cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))  

#Detect coord orange
  if len(contours) != 0:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            find_cor()
            file = open("otus.txt", "a+")
            file.write('4 ' +  str(x) + ' ' + str(y)  + '\n')  
            file.close()            
            x4=x
            y4=y

# Contour for purple color
  contours, hierarchy = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      #cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))  

#Detect coord purple
  if len(contours) != 0:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            find_cor()
            file = open("otus.txt", "a+")
            file.write('5 ' +  str(x) + ' ' + str(y)  + '\n')  
            file.close()            
            x5=x
            y5=y    

  break  
    
# Program Termination
cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
if cv2.waitKey(0) :
#cap.release()
  cv2.destroyWindow("imageFrame")
  #break



while(1):
  
  _, imageFrame = webcam.read()
  hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

  # Red color and mask
  red_lower = np.array([145, 50, 150], np.uint8)
  red_upper = np.array([180, 255, 255], np.uint8)
  red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

  
  kernal = np.ones((5, 5), "uint8")
  
  # For red color
  red_mask = cv2.dilate(red_mask, kernal)
  res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)
  
  
  # Contour for red color
  contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      #cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))  

#Detect coord red
  if len(contours) != 0:
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            find_cor()
            file = open("otus.txt", "a+")
            file.write('0 ' +  str(x) + ' ' + str(y)  + '\n') 
            file.close()
            x0=x
            y0=y
            if deltax0_x1>abs(x0-x1):
              deltax0_x1=abs(x0-x1)
              x0_g=x0
            if deltay0_y1>abs(y0-y1):
              deltay0_y1=abs(y0-y1)
              y0_g=y0
            if deltax0_x2>abs(x0-x2):
              deltax0_x2=abs(x0-x2)
              x0_b=x0
            if deltay0_y2>abs(y0-y2):
              deltay0_y2=abs(y0-y2)
              y0_b=y0

            #if deltax0_x3>abs(x0-x3):
              #deltax0_x3=abs(x0-x3)
              #x0_y=x0
            #if deltay0_y3>abs(y0-y3):
              #deltay0_y3=abs(y0-y3)
              #y0_y=y0

            if deltax0_x4>abs(x0-x4):
              deltax0_x4=abs(x0-x4)
              x0_o=x0
            if deltay0_y4>abs(y0-y4):
              deltay0_y4=abs(y0-y4)
              y0_o=y0

            if deltax0_x5>abs(x0-x5):
              deltax0_x5=abs(x0-x5)
              x0_p=x0
            if deltay0_y5>abs(y0-y5):
              deltay0_y5=abs(y0-y5)
              y0_p=y0
            
  # Program Termination
  cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
  if cv2.waitKey(10) & 0xFF == ord('q'):
    webcam.release()
    cv2.destroyAllWindows()
    break


kor1=gomografia(x1,y1)
x1_1=kor1[0][0][0]
y1_1=kor1[0][0][1]
kor2=gomografia(x2,y2) 
x2_2=kor2[0][0][0]
y2_2=kor2[0][0][1]

#kor3=gomografia(x3,y3)
#x3_3=kor3[0][0][0]
#y3_3=kor3[0][0][1]

kor4=gomografia(x4,y4)
x4_4=kor4[0][0][0]
y4_4=kor4[0][0][1]

kor5=gomografia(x5,y5)
x5_5=kor5[0][0][0]
y5_5=kor5[0][0][1]



kor0_g=gomografia(x0_g,y0_g)
x_g=kor0_g[0][0][0]
y_g=kor0_g[0][0][1]
kor0_b=gomografia(x0_b,y0_b) 
x_b=kor0_b[0][0][0]
y_b=kor0_b[0][0][1]

#kor3=gomografia(x3,y3)
#x3_3=kor3[0][0][0]
#y3_3=kor3[0][0][1]

kor0_o=gomografia(x0_o,y0_o)
x_o=kor0_o[0][0][0]
y_o=kor0_o[0][0][1]

kor0_p=gomografia(x0_p,y0_p)
x_p=kor0_p[0][0][0]
y_p=kor0_p[0][0][1]




print ('Distance between robot and green x = ', abs(x1_1-x_g),' y = ', abs(y1_1-y_g),'\n')
print ('Distance between robot and blue = ', abs(x2_2-x_b),' y = ', abs(y2_2-y_b),'\n')
#print ('Distance between robot and yellow = ', math.sqrt(deltax0_x3*deltax0_x3+deltay0_y3*deltay0_y3),'\n')
print ('Distance between robot and orange = ', abs(x4_4-x_o),' y = ', abs(y4_4-y_o),'\n')
print ('Distance between robot and purple = ', abs(x5_5-x_p),' y = ', abs(y5_5-y_p),'\n')


