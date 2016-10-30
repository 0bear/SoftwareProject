import numpy as np
import cv2
import os

camera = cv2.VideoCapture(0)
namecount = 0
dircount = 0
dirname = 0

while(camera.isOpened()):

    ret = camera.read()

    if ret[0] == True:
        saveimage = cv2.resize(ret[1],(320 ,240))

        if not os.path.isdir("./" + str(dirname) + "/"):
            os.mkdir("./" + str(dirname) + "/")

        cv2.imwrite("./" + str(dirname) + "/"+ "test_" + str(namecount) + ".jpg", saveimage)

        namecount = namecount + 1
        dircount = dircount + 1

        if dircount == 8191:
            dirname = dirname + 1
            dircount = 0
            namecount = 0

# Wait 100ms for key input. If q is pressed, break.
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    else:
        break

# Release everything if job is finished
camera.release()
saveimage.release()
cv2.destroyAllWindows()
