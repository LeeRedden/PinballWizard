# import numpy as np
# import cv2
# import time

# cap = cv2.VideoCapture(0)

# count = 100

# while(count):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     try:
#         cv2.imshow('frame',gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     except: 
#         print "frame wasn't captures correctly"
        
#     count -= 1
#     time.sleep(0.1)
    
    
# cap.release()
# #out.release()
# cv2.destroyAllWindows()

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
