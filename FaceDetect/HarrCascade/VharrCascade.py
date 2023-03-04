

#  python VharrCascade.py --cascade haarcascade_frontalface_default.xml


# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")

args = vars(ap.parse_args())

# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier(args["cascade"])
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
total = 0
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, clone it, (just
	# in case we want to write it to disk), and then resize the frame
	# so we can apply face detection faster
	frame = vs.read()
	frame = imutils.resize(frame, width=700)
	# detect faces in the grayscale frame
	rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30)
		)
	# loop over the face detections and draw them on the frame
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		
    # show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	
	k = cv2.waitKey(1)
	if k==ord("q"):
		print("Escape hit, closing...")
		break
	elif k==ord("k"):
    	# SPACE pressed
		img_name = "opencv_frame_{}.png".format(total)
		cv2.imwrite(img_name, frame)
		print("{} fatto!".format(img_name))
		total += 1
    				
# print the total faces saved and do a bit of cleanup
print("[INFO] {} face images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()



	