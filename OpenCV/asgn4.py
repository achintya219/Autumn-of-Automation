import cv2 as cv

shapes = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/shapes.jpg")

shapesbw = cv.Canny(shapes, 100, 200)
shapesbw = cv.GaussianBlur(shapesbw, (15,15), 0)

cv.imshow("Display Window", shapesbw)
cv.waitKey(0)

contours, hierarchy = cv.findContours(shapesbw, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours2 = (contours[1], contours[2], contours[3], contours[4], contours[5], contours[8])

font = cv.FONT_HERSHEY_COMPLEX

for cnt in contours2:
	apprx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt, True), True)
	cv.drawContours(shapes, [apprx], 0, (0, 255, 255), 3)
	x = apprx.ravel()[0]
	y = apprx.ravel()[1]
	if len(apprx) == 3:
		cv.putText(shapes, "Traingle", (x,y), font, 0.5, (0))
	elif len(apprx) == 4:
		x, y, w, h = cv.boundingRect(apprx)
		aspectRatio = float(w)/h
		if 0.95 <= aspectRatio <= 1.05:
			cv.putText(shapes, "Square", (x,y), font, 0.5, (0))
		else:
			if -3 < apprx.ravel()[3] - apprx.ravel()[7] < 3 and -3 < apprx.ravel()[0] - apprx.ravel()[4] < 3:
				cv.putText(shapes, "Diamond", (x, y), font, 0.5, (0))
			else:
				cv.putText(shapes, "Rectangle", (x,y), font, 0.5, (0))
	elif 6 < len(apprx) < 15:
		cv.putText(shapes, "Elipse", (x,y), font, 0.5, (0))
	else:
		cv.putText(shapes, "Circle", (x,y), font, 0.5, (0))

cv.imshow("Display Window", shapes)
cv.waitKey(0)
cv.destroyAllWindows()

