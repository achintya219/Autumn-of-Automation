import cv2 as cv

nemo = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/nemo3.jpg")

nemo = cv.cvtColor(nemo, cv.COLOR_BGR2RGB)

cv.imshow("Display Window", nemo)
cv.waitKey(0)