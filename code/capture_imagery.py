# Data capture
import datetime
import errno
import os
import sys
import time
import webcam


def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


# Define function for capturing datasets using webcam
def capture_image_set(number_of_images, directory, sleep_time=3):
	if os.path.exists(directory)
		print directory
	else:
		print "--------- ERROR: invalid directory ----------"
		print directory
		sys.exit()

	for i in range(number_of_images):
		# Beep to say an image is being saved
		sys.stdout.write('\a')
		sys.stdout.flush()
		# Save image
		image_capture.save(directory)
		# Sleep till next image capture
		time.sleep(sleep_time)


# Initialize webcam
image_capture = webcam.webcam()
# Sleep to let the webcam initialize
time.sleep(0.1)

# Setting up the folder structure for saving the imagery
# Get directory of this script file
main_directory = os.getcwd()

room_types = ["kitchen", "living_room", "dining_room"]
for room_type in room_types:
	ensure_path(os.path.join(main_directory, "imagery", "room_type"))


# Example function call to capture an image set
# This function should be modified according to what dataset you want to collect
capture_image_set(15, os.path.join(main_directory, "imagery", "kitchen"))
