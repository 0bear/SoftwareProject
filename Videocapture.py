import cv2
import numpy as np

# frame per second = 15
# resolution = 1024*768

camera = cv2.VideoCapture(0)
out = cv2.VideoWriter('Output.mp4', -1, 15.0, (1024,768))

while(camera.isOpened):
        ret, frame = camera.read()
        if ret[0] == True:
            frame = cv2.flip(frame,0)
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitkey(1) & 0xFF ==or('q'):
                break

        else:
            break
            camera.release()
            out.release()
            cv2.destroyAllWindows()
