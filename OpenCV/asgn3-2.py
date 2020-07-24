import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	frame = cv.GaussianBlur(frame, (3,3), 0)

	frame = cv.Laplacian(frame, -1, ksize=5)

	frame = 255 - frame

	ret1, frame = cv.threshold(frame, 150, 255, cv.THRESH_BINARY)
	
	cv.imshow('Frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()