# This class tries to mimich the tensorflow mnist reader and writer
# 
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#
# expects a folder="folder" where subfolders are classes and in those subfolders are images 
# with the ending "imgtype"
# 
# folder/class1/1.bmp
# folder/class1/2.bmp
# folder/class2/1.bmp
# folder/class2/2.bmp
# folder/class2/3.bmp

import numpy as np
import random
import cv2
import os
import collections

class reader(object):
    def __init__(self, folder, height=28, width=28, imgtype=".bmp"):
        random.seed("42")
        
        self.folder = folder
        self.height = height
        self.width = width
        self.imgtype = imgtype
        self.count = 0

        # populate classes
        self.classNames = sorted(os.listdir(folder))
        
        self.classes = collections.defaultdict(list)
        for name in self.classNames:
            classFolder = os.path.join(folder, name)
            for file in os.listdir(classFolder):
                if file.endswith(imgtype):
                    self.classes[name].append(file)

    def num_classes(self):
    	return len(self.classNames)

    def print_classes(self):
        for className in self.classNames:
            print className, len(self.classes[className])
            
    def print_files(self):
        for className in self.classNames:
            print className, len(self.classes[className])
            print self.classes[className]
    
    def _read_image(self, path):    
    	# read image
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, (self.width, self.height), interpolation=cv2.INTER_CUBIC)
        reshape = resize.reshape((1, self.height*self.width))
        return reshape/255.0


    def next_batch(self, batch_size):
        self.count += batch_size
        
        data = np.zeros((batch_size, self.width*self.height))
        labels = np.zeros((batch_size, self.num_classes()))
        
        for idx in xrange(batch_size):
            c = random.randrange(self.num_classes())
            className = self.classNames[c]
            
            img_idx = random.randrange(len(self.classes[className]))
            path = os.path.join(self.folder, className, self.classes[className][img_idx])
            
            labels[idx, c] = 1
            data[idx, :] = self._read_image(path)
            
        return data, labels

    def all(self):
    	num_images = 0
    	for name in self.classNames:
    		num_images += len(self.classes[name])

    	data = np.zeros((num_images, self.width*self.height))
        labels = np.zeros((num_images, self.num_classes()))

        idx = 0

        for class_idx in xrange(self.num_classes()):
        	class_name = self.classNames[class_idx]
        	for file_name in self.classes[class_name]:
        		path = os.path.join(self.folder, class_name, file_name)
        		labels[idx,class_idx] = 1
        		data[idx,:] = self._read_image(path)
        		idx += 1

        return data, labels

        