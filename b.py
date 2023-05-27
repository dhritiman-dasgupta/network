# import the opencv library
import cv2
import imutils
from imutils.video import VideoStream
from ultralytics import YOLO
model=YOLO("yolov8x.pt")
model.predict(source="aa.jpg",show=True,line_width=1,conf=0.5,classes=0)
