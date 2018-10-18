# -*- coding: utf-8 -*-

import cv2


print(cv2.__version__)
#cap = cv2.VideoCapture(0)




cascade_src = 'cars.xml'
#video_src = image_np
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, image_np = cap.read()
    if (type(image_np) == type(None)):
        break
    
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(image_np,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('video', cv2.resize(image_np, (800,600)))
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
