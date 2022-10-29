from tkinter.tix import Tree
import cv2 as cv
from cv2 import aruco
import numpy as np

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)

param_marker = aruco.DetectorParameters_create() # function to create a parameter to detect aruco marker

# to acess the webcam to scan the aruco marker

cam=cv.VideoCapture(0)

while True:
    ret, frame=cam.read()
    if not ret:
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)# picture converted to grayscale as it requires less processing power
    marker_corner,marker_ID,reject=aruco.detectMarkers(gray,marker_dict,parameters=param_marker)
    if marker_corner:
        for id ,corners in zip(marker_ID,marker_corner):
            cv.polylines(frame,[corners.astype(np.int32)],True,(255,255,0),4,cv.LINE_AA)#to define proper borders whle scanning markers
            corners=corners.reshape(4,2)#reshaping the aruco marker size using numpy
            corners=corners.astype(int)
            top_right = corners[0].ravel()
            cv.putText(frame,f'Aruco marker ID :{id[0]}',top_right,cv.FONT_HERSHEY_PLAIN,fontScale=1.7,color=(255,0,0) ,thickness=2,lineType=cv.LINE_AA)

    cv.imshow('frame',frame)
    key = cv.waitKey(1)
    if key ==ord('q'): # when pressed  key Q on the keyboard the camera is closed
        break
cam.release()
cv.destroyAllWindows()