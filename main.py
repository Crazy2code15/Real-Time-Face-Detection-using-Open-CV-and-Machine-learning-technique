# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:55:25 2021

@author: vishwajeet
"""

"import numpy as np"
import cv2
"import sys"
x = input(str("Do you want to detect face live or in an image?" ))
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if x == "image":
    image_path = input(str("Please enter Image path"))
    img = image_path

    image = cv2.imread(img)
    height, width,_ = image.shape
    img_gray = cv2.imread(img,0)

    faces = face_cascade.detectMultiScale(img_gray)
    print(type(faces))
    if len(faces) == 0:
        print("No faces found")
    else:
        number_faces = faces.shape[0]
    
    for (x,y,w,h) in faces:
        if w>0.4*width or h>0.4*height or (w*h)>0.2*(height*width):
                number_faces= number_faces-1
                continue
        else:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)
    print("Number of faces detected: " + str(number_faces))
    
    cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1)
    
    cv2.imshow('Image with faces',cv2.resize(image,(600,600)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if x=="live":
    video_capture = cv2.VideoCapture(0)
   
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30))
    
        if len(faces) == 0:
            print("No faces found")
            print("\n")
            continue  
    video_capture.release()
else:
    
        print("Number of faces detected: " + str(faces.shape[0]))
        print("\n")
        cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1)
        
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
            # Display the resulting frame
            cv2.imshow('Video', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                exit()
    # When everything is done, release the capture
        
cv2.destroyAllWindows()