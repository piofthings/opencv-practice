#!/usr/bin/env python3
import numpy as np
import cv2 as cv
import time

img = cv.imread('/home/pi/Pictures/All.jpg',cv.IMREAD_COLOR)
blurred_res = cv.medianBlur(img,5)
gray = cv.cvtColor(blurred_res,cv.COLOR_BGR2GRAY)

circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,
                            param1=70,param2=55,minRadius=1 ,maxRadius=350)
font = cv.FONT_HERSHEY_SIMPLEX

if circles is not None:
	circles = np.uint16(np.around(circles))
	height, width = img.shape[:2]   

	for i in circles[0,:]:
		# draw the outer circle
		cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
		# draw the center of the circle
		cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
		cv.putText(img,'Center[x y radius]: ' + str(i),(i[0]+10,i[1]+i[2]), font, 0.5, (200,255,155), 1, cv.LINE_AA)

	cv.putText(img,'Circles count: ' + str(circles[0,:].size/3),(10,100), font, 0.5, (200,255,155), 1, cv.LINE_AA)

cv.imshow('detected circles',img)
cv.waitKey(0)
cv.destroyAllWindows()
