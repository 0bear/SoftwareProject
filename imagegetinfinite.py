import numpy as np
import cv2

camera = cv2.VideoCapture(0)
num = 0

while(camera.isOpened()):

    ret = camera.read()

    if ret[0] == True:
        frame = cv2.flip(frame,0)
        cv2.imshow('Webcam',frame)
        cv2.imwrite("test_" + str(num) + ".jpg", ret[1])

        num = num + 1

# Wait 100ms for key input. If q is pressed, break.
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    else:
        break

# Release everything if job is finished
camera.release()
cv2.destroyAllWindows()
