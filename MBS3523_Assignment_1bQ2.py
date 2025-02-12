import cv2
import numpy as np

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
width = cam.get(3)
height = cam.get(4)
print(height,width)

while True:
    ret, frame = cam.read()
    frameResize = cv2.resize(frame, (480,360))
    #frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameBlur = cv2.GaussianBlur(frame, (15, 15), 0)
    frameCanny = cv2.Canny(frame, 100, 200)

    cv2.imshow('cam', frame)
    cv2.imshow('camHSV', frameHSV)
    cv2.imshow('camBlur', frameBlur)
    cv2.imshow('camCanny', frameCanny)
    #cv2.imshow('camGray', frameGray)
    #cv2.imshow('camResize', frameResize)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()