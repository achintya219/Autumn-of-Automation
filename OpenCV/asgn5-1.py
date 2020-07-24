import cv2 as cv
import numpy as np

cap = cv.VideoCapture("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/leomessi.mp4")
while(True):
	ret, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	gray_blur = cv.blur(gray, (3, 3))

	detected_circles = cv.HoughCircles(gray_blur, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=60)
	flag = 0
	if detected_circles is not None:
		detected_circles = np.uint16(np.around(detected_circles))

		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]

			cv.circle(frame, (a, b), r, (0, 255, 0), 5)
			cv.imshow('Frame', frame)
			if cv.waitKey(40) & 0xFF == ord('q'):
				flag = 1
				break
	else:
		cv.imshow('Frame', frame)
		if cv.waitKey(40) & 0xFF == ord('q'):
			break
	if flag == 1:
		break

cap.release()
cv.destroyAllWindows()