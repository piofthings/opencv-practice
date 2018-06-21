import numpy as np
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)
start_time = time.time() ' Timer start
frames_per_second = 5 'Frames per second
frameIndex = 0

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    height, width = frame.shape[:2]   
     
    cv2.imshow('frame',frame)
    
    now = time.time() ' Timer start
    if(now-start_time) >= (1/frames_per_second): 'If time difference matches fps set
        cv2.putText(frame,'Frame: ' + str(frameIndex) + ': ' + str(now),(10,height-20), font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.imwrite('/home/pi/Pictures/recording/frame' + str(frameIndex) + '.jpg', frame)
        frameIndex += 1
        start_time = now ' Reset timer
    
    if cv2.waitKey(1) & 0xFF == ord('q'):        
        break

cap.release()
cv2.destroyAllWindows()
