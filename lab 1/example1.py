import cv2
import numpy as np


img = cv2.imread('lena.png',cv2.IMREAD_UNCHANGED)
cv2.imshow('input image',img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define the color range in HSV
lower_value = np.array([170,10,50])
upper_value = np.array([205,255,255])

# Threshold HSV image to get only selected colors
mask = cv2.inRange(hsv, lower_value, upper_value)

# AND operation of the input image and mask
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('thresholded components',res)

cv2.imwrite('modified_lena.jpg', res, [cv2.IMWRITE_JPEG_QUALITY, 100])


cv2.waitKey(0)
cv2.destroyAllWindows()