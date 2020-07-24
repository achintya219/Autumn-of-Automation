import cv2 as cv


nemo = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/nemo3.jpg")

cv.imshow("Display Window", nemo)
cv.waitKey(0)

#Converting image to greyscale and black and white
greynemo = cv.cvtColor(nemo, cv.COLOR_BGR2GRAY)
cv.imshow("Display Window", greynemo)
cv.waitKey(0)

#using global otsu thresholding
ret, th1 = cv.threshold(greynemo, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Display Window", th1)
cv.waitKey(0)

#using adaptive thresholding
bwnemo = cv.adaptiveThreshold(greynemo, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Display Window", bwnemo)
cv.waitKey(0)

cv.destrolAllWindows()