import numpy as np
import cv2


cap=cv2.VideoCapture(0)

while(True):
    ret, frame=cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred_frame = cv2.GaussianBlur(blurred_frame,(5,5),0)

    

    circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10)

    if circles is not None and len(circles)==1:
        print(circles)
        x=circles[0][0]
        y=circles[0][1]
        r=circles[0][2]
        
cap.release()

cv2.destroyAllWindows()
    
    
    
    





