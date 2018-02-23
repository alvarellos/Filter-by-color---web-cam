import cv2
import numpy as np
 
# Initialize webcam
cap = cv2.VideoCapture(0)
 
# define two red ranges in HSV
lower_red= np.array([165,0,0])
upper_red = np.array([180,255,255])
 
lower_red1 = np.array([0,0,0])
upper_red1 = np.array([15,255,255])
 
# loop until break statement is executed
# (165 to 0) or (0 to 15).
while True:
    
    # Read webcam image
    ret, frame = cap.read()
    
    # Convert image from RBG/BGR to HSV so we easily filter
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # Use inRange to capture only the values between lower & upper_purple
    mask = cv2.inRange(hsv_img, lower_red, upper_red)
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
 
    # Perform Bitwise AND on mask and our original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)
 
    # Combine the two filtered mask and use bitwise_or to merge them.
    res2 = cv2.bitwise_or(res, res1)
    
    cv2.imshow('Original', frame)  
    cv2.imshow('mask', mask)
    cv2.imshow('Red Range 1 Only', res)
    cv2.imshow('Red Range 2 Only', res1)
    cv2.imshow('Filtered Red Only', res2)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()