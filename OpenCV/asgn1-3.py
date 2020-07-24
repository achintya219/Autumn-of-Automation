import cv2 as cv

nemo = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/nemo3.jpg")

lower = (150, 0, 0)
upper = (255, 150, 50)

mask = cv.inRange(nemo, lower, upper)
nemo[mask != 0] = [0, 0, 255]

cv.imshow("Display Window", nemo)
cv.waitKey(0)