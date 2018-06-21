#import cv2
#import numpy as np
#from matplotlib import pyplot as pltimport

#img = cv2.imread('/home/pi/Pictures/hack-horsham.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imwrite('/home/pi/Pictures/hack-horsham2.jpg', img)
    
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/pi/Pictures/hack-horsham.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()