#!/usr/bin/env python3
import numpy as np
import cv2 as cv
import time
    
img = cv.imread('/home/pi/Pictures/All.jpg',cv.IMREAD_COLOR)
window_name = "HSV Colour tracker"

font = cv.FONT_HERSHEY_SIMPLEX
initialised = False
# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	
red_hsv    = [np.array([  0, 125, 102]),np.array([  8, 255, 255])]
green_hsv  = [np.array([ 49, 115,  70]),np.array([ 98, 237, 255])]
blue_hsv   = [np.array([ 96,  92,  77]),np.array([129, 255, 255])]
yellow_hsv = [np.array([ 20,  91, 126]),np.array([ 43, 228, 255])]

# Hough Circle params
dp = 1
min_dist = 20
param1 = 30
param2 = 60
min_radius = 1
max_radius = 350


cv.namedWindow(window_name)
mask = cv.inRange(hsv, blue_hsv[0], blue_hsv[1])
#mask = cv.bitwise_not(mask)
display_img = cv.bitwise_and(img,img, mask= mask)
blurred_res = cv.medianBlur(display_img, 5)
gray = cv.cvtColor(blurred_res, cv.COLOR_BGR2GRAY)

def update_circles():
	if initialised == True:
		circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,
                            param1=30,param2=60,minRadius=1 ,maxRadius=350)    
		print(str(dp) + " " + str(min_dist) + " " + str(param1) + " " + str(param2) + " " + str(min_radius) + " " + str(max_radius))
		if circles is not None:
			circles = np.uint16(np.around(circles))
			height, width = blurred_res.shape[:2]   
			print("Number of circles: " + str(circles[0,:].size/3))

			for i in circles[0,:]:
				# draw the outer circle
				cv.circle(display_img,(i[0],i[1]),i[2],(0,255,0),2)
				# draw the center of the circle
				cv.circle(display_img,(i[0],i[1]),2,(0,0,255),3)
				cv.putText(display_img,'Center[x y radius]: ' + str(i),(i[0]+10,i[1]+i[2]), font, 0.5, (200,255,155), 1, cv.LINE_AA)

		cv.imshow(window_name,display_img)
	
def set_dp (x) :
	dp = x
	update_circles()
	
def set_min_dist(x) :
	min_dist = x
	update_circles()
	
def set_param1(x) :
	param1 = x
	update_circles()
	
def set_param2(x):
	param2 = x
	update_circles()
	
def set_min_radius (x):
	min_radius = x
	update_circles()
	
def set_max_radius (x) :
	max_radius = x
	update_circles()
	
def nothing (x) :
	pass
	
# create trackbars 
cv.createTrackbar('DP',window_name,0,4,set_dp)
cv.setTrackbarPos('DP',window_name, dp)
cv.createTrackbar('min_dist',window_name,0,255,set_min_dist)
cv.setTrackbarPos('min_dist',window_name, min_dist)
cv.createTrackbar('param1',window_name,0,255, set_param1)
cv.setTrackbarPos('param1',window_name, param1)
cv.createTrackbar('param2',window_name,0,255,set_param2)
cv.setTrackbarPos('param2',window_name, param2)
cv.createTrackbar('min_radius',window_name,0,255,set_min_radius)
cv.setTrackbarPos('min_radius',window_name, min_radius)
cv.createTrackbar('max_radius',window_name,0,500,set_max_radius)
cv.setTrackbarPos('max_radius',window_name, max_radius)

initialised = True
update_circles()

cv.waitKey(0)
cv.destroyAllWindows()

	
