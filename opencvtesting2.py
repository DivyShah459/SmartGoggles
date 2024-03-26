import numpy as np
import cv2 as cv
im = cv.imread('brailleimages/server.jpg')
im = cv.resize(im,(640,640))
assert im is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(contours)
cnt = contours[4]
cv.imshow("Image", im)
cv.drawContours(im, [cnt], 0, (0,255,0), 3)

cv.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv.destroyAllWindows()