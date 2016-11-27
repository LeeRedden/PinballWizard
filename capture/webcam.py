import numpy as np
import cv2
import time


class webcam(object):
    def __init__(self, device=0, height=100, width=100, interpolation=cv2.INTER_CUBIC):
        print "here"
        self.cap = cv2.VideoCapture(device)
        self.height = height
        self.width = width
        self.interpolation = interpolation
        self.count = 0

    def image(self):
        self.count += 1
        ret, frame = self.cap.read()
        if ret:
            resize = cv2.resize(frame, (self.width, self.height), interpolation=self.interpolation)
            return resize, self.count
        else: 
            print "error in webcam captureing image"

    def show(self):
        frame, count = self.image()

        windowName = "%d" % count
        cv2.imshow(windowName, frame)
        cv2.waitKey(0)

        cv2.waitKey(5)
        cv2.destroyWindow(windowName)
        cv2.waitKey(5)

    def close(self):
        self.cap.release()
