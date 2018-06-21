import numpy as np
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)
start_time = time.time()
frames_per_second = 5
frameIndex = 0

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, raw_frame = cap.read()
    frame = cv2.cvtColor(raw_frame, cv2.IMREAD_COLOR)
    height, width = frame.shape[:2]   
     
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):  
        cv2.putText(frame,'Frame: ' + str(frameIndex) + ': ' + str(datetime.datetime.now()),(10,height-20), font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.imwrite('/home/pi/Pictures/recording/frame' + str(frameIndex) + '.jpg', frame)
        frameIndex += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):        
        break

cap.release()
cv2.destroyAllWindows()

