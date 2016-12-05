# Capture Imagere capture
import argparse
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
def capture_image_set(image_source, number_of_images, directory, sleep_time=3):
	ensure_path(directory)

	for i in range(number_of_images):
		# Beep to say an image is being saved
		sys.stdout.write('\a')
		sys.stdout.flush()

		image_source.save(directory)
		print "captured image: %d" % (i)

		time.sleep(sleep_time)


parser = argparse.ArgumentParser(description='Capture Imagery for a machine learning system')

parser.add_argument('room', type=str, help='kitchen, living_room, or dining_room')
parser.add_argument('--count', type=int, default=15, help='number of images to capture in a single session')
parser.add_argument('--delay', type=float, default=3.0, help='seconds between image capture')

args = parser.parse_args()
print "captureing %d images" % (args.count)
print " room: %s" % (args.room)
print " with %d seconds between images" % (args.delay)

if args.room not in ["kitchen", "living_room", "dining_room"]:
	print "room not a stardard room"

# wait 5 seconds before captureing the room
time.sleep(5)

path = os.path.join(os.getcwd(), "imagery", args.room)
capture_image_set(webcam.webcam(), args.count, path, sleep_time=args.delay)
