import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('output.avi', -1 , 20.0, (640,480))
count = 20 # 1sec
while(cap.isOpened() and out.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.waitKey(50)

	if count == 0:
            break

	count = count - 1
    else:
        break
else:
    print "err"

# Release everything if job is finished
cap.release()
out.release()
