import cv2 as cv
import numpy as np

t = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/Timage.png")

cv.imshow("Display Window", t)
cv.waitKey(0)
rows, cols, color = t.shape

#Translation images

M = np.float32([[1, 0, 100], [0, 1, 50]])
t2 = cv.warpAffine(t, M, (cols, rows))

cv.imshow("Display Window", t2)
cv.waitKey(0)

M = np.float32([[1, 0, -100], [0, 1, -50]])
t3 = cv.warpAffine(t, M, (cols, rows))

cv.imshow("Display Window", t3)
cv.waitKey(0)

M = np.float32([[1, 0, -100], [0, 1, 50]])
t4 = cv.warpAffine(t, M, (cols, rows))

cv.imshow("Display Window", t4)
cv.waitKey(0)

M = np.float32([[1, 0, 100], [0, 1, -50]])
t5 = cv.warpAffine(t, M, (cols, rows))

cv.imshow("Display Window", t5)
cv.waitKey(0)


#Rotation
M = cv.getRotationMatrix2D((cols/4, rows/4), 45, 1)
t6 = cv.warpAffine(t, M, (cols, rows))
cv.imshow("Display Window", t6)
cv.waitKey(0)

M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
t6 = cv.warpAffine(t, M, (cols, rows))
cv.imshow("Display Window", t6)
cv.waitKey(0)

M = cv.getRotationMatrix2D((cols/2, rows/2), -90, 1)
t6 = cv.warpAffine(t, M, (cols, rows))
cv.imshow("Display Window", t6)
cv.waitKey(0)

M = cv.getRotationMatrix2D((cols/2, rows/2), 135, 1)
t6 = cv.warpAffine(t, M, (cols, rows))
cv.imshow("Display Window", t6)
cv.waitKey(0)

#blurring
kernel = np.ones((3,3), np.float32)/9
t2 = cv.filter2D(t, -1, kernel)
cv.imshow("Display Window", t2)
cv.waitKey(0)

blur = cv.blur(t, (4, 4))
cv.imshow("Display Window", blur)
cv.waitKey(0)

blur = cv.bilateralFilter(t, 9, 75, 75)
cv.imshow("Display Window", blur)
cv.waitKey(0)


