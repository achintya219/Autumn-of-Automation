import cv2 as cv
import numpy as np

img = cv.imread("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/ball.jpg")
cap = cv.VideoCapture("/home/achintya/Desktop/Autumn-of-Automation/OpenCV/leomessi.mp4")


orb = cv.ORB()
kp_image, desc_image = orb.detectAndCompute(img, None)



index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params= dict()

flann = cv.FlannBasedMatcher(index_params, search_params)

while(True):
	ret, frame = cap.read()
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	
	kp_gray, desc_gray  = orb.detectAndCompute(gray, None)

	matches = flann.knnMatch(desc_image, desc_gray, k=2)
	
	good_points = []
	for m, n in matches:
		if m.distance  < 0.7*n.distance:
			good_points.append(m)

	
	MIN_MATCH_COUNT = 10
	if len(good_points) > MIN_MATCH_COUNT:
		query_pts = np.float32([ kp_image[m.queryIdx].pt for m in good_points ]).reshape(-1, 1, 2)
		train_pts = np.float32([ kp_gray[m.trainIdx] for m in good_points ]).reshape(-1, 1, 2)

		M, mask = cv.findHomography(query_pts, train_pts, cv.RANSAC, 5.0)
		matchesMask = mask.ravel().tolist()

		h, w = img.shape
		pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1 , 2)
		dst = cv.perspectiveTransform(pts, M)

		gray = cv.polylines(frame, [np.int32(dst)], True, 255, 3, cv.LINE_AA)

		draw_params = dict(matchColor = (0, 255, 0), singlePointColor=None, matchesMask = matchesMask, flags=2)

		img3 = cv.drawMatches(img, kp_image, gray, kp_gray, good_points, None, **draw_params)

		cv.imshow("frame", img3)
	else:
		cv.imshow("frame", frame)
	
	if cv.waitKey(40) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()