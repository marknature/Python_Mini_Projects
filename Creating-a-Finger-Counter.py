# Creating a Finger Counter Using Computer Vision and OpenCv in Python
# https://www.geeksforgeeks.org/creating-a-finger-counter-using-computer-vision-and-opencv-in-python/?ref=lbp

import cv2 
from cvzone.HandTrackingModule import HandDetector 

detector = HandDetector(maxHands=1, detectionCon=0.8) 
video = cv2.VideoCapture(1) 

while True: 
	_, img = video.read() 
	img = cv2.flip(img, 1) 
	hand = detector.findHands(img, draw=False) 
	fing = cv2.imread("Put image path with 0 fingures up") 
	if hand: 
		lmlist = hand[0] 
		if lmlist: 
			fingerup = detector.fingersUp(lmlist) 
			if fingerup == [0, 1, 0, 0, 0]: 
				fing = cv2.imread("Put image \ 
				path of 1 fingures up") 
			if fingerup == [0, 1, 1, 0, 0]: 
				fing = cv2.imread("Put image \ 
				path of 2 fingures up") 
			if fingerup == [0, 1, 1, 1, 0]: 
				fing = cv2.imread("Put image \ 
				path of 3 fingures up") 
			if fingerup == [0, 1, 1, 1, 1]: 
				fing = cv2.imread("Put image \ 
				path of 4 fingures up") 
			if fingerup == [1, 1, 1, 1, 1]: 
				fing = cv2.imread("Put image \ 
				path of 4 fingures and thumbs up") 
	fing = cv2.resize(fing, (220, 280)) 
	img[50:330, 20:240] = fing 
	cv2.imshow("Video", img) 
	
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break
		
video.release() 
cv2.destroyAllWindows() 
