import cv2

camera = cv2.VideoCapture(0)

if camera.isOpened() == True:
    ret = camera.read()
    if ret[0] == True:
        cv2.imwrite("test.jpg", ret[1])
        camera.release()
