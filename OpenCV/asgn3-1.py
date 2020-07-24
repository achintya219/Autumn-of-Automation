import cv2 as cv

nemo = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/nemo3.jpg")
nemo = cv.cvtColor(nemo, cv.COLOR_BGR2GRAY)

nemo = cv.GaussianBlur(nemo, (3,3), 0)

nemo = cv.Laplacian(nemo, -1, ksize=5)

nemo = 255 - nemo

ret, nemo = cv.threshold(nemo, 150, 255, cv.THRESH_BINARY)

cv.imshow("Display Window", nemo)
cv.waitKey(0)

cv.destroyAllWindows()

