import cv2
import numpy as np
import os
import time


class webcam(object):
    def __init__(self, device=0, height=100, width=100, interpolation=cv2.INTER_CUBIC):
        self.cap = cv2.VideoCapture(device)
        time.sleep(0.1) # this devide isn't ready to use for a certain amount of time

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

    def save(self, directory):
        frame, count = self.image()
        current_time = time.strftime("%Y%m%d%H%M%S")
        cv2.imwrite( os.path.join(directory, "%s-%d.bmp" % (current_time, count)), frame)

    def close(self):
        self.cap.release()
        