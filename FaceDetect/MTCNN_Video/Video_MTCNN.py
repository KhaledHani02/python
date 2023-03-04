
from imutils.video import VideoStream
import time
from mtcnn import MTCNN
import cv2
import imutils

def draw_faceboxCV(data, result_list):

    for result in result_list:

        (x, y, width, height )= result['box']
        cv2.rectangle(data, (x, y), (x+width, y+height), (0, 0, 255), 2)



print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
total=0
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    detector = MTCNN(min_face_size = 5)
    faces = detector.detect_faces(frame)
    if len(faces)!=0:
        draw_faceboxCV(frame,faces)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    elif key==ord("k"):
        img_name = "frame_{}.png".format(total)
        images=cv2.imwrite(img_name, frame)
        print("{} fatto!".format(img_name))
        total += 1
    		


	
	