# Data capture
import os
import webcam
import datetime, time
import sys

# Initialize webcam
image_capture = webcam.webcam()
# Sleep to let the webcam initialize
time.sleep(.1)

# Define function for capturing datasets using webcam
def capture_image_set(number_of_images, type):
	if type == "kitchen":
		storage_dir = os.getcwd() + "/imagery/kitchen/"
	elif type == "living_room":
		storage_dir = os.getcwd() + "/imagery/living_room/"
	elif type == "dining_room":
		storage_dir = os.getcwd() + "/imagery/dining_room/"

	try:
		print storage_dir
	except:
		print "--------- ERROR: invalid directory ----------"
		sys.exit()

	for i in range(number_of_images):
		# Beep to say an image is being saved
		sys.stdout.write('\a')
		sys.stdout.flush()
		# Save image
		image_capture.save(storage_dir)
		# Sleep till next image capture
		time.sleep(3)

# Setting up the folder structure for saving the imagery
# Get directory of this script file
main_directory = os.getcwd()

# Make imagery root folder
imagery_directory = main_directory + "/imagery"
if not os.path.isdir(imagery_directory):
	os.makedirs(imagery_directory)

# create kitchen, living_room, and dining_room folders
folder_dir = imagery_directory + "/kitchen/"
if not os.path.isdir(folder_dir):
	os.makedirs(folder_dir)

folder_dir = imagery_directory + "/living_room/"
if not os.path.isdir(folder_dir):
	os.makedirs(folder_dir)

folder_dir = imagery_directory + "/dining_room/"
if not os.path.isdir(folder_dir):
	os.makedirs(folder_dir)

# Example function call to capture an image set
# This function should be modified according to what dataset you want to collect
capture_image_set(15, "kitchen")





