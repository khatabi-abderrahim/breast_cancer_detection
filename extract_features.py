import cv2
import numpy
from tasks import get_texture_glcm_measurements

"""
Script to extract the features from the image
"""
"""
Call the function that will delegate the GLCM vertical relationship
calculations in an asynchronous way.
"""

for image_number in range(1,323):
	image_file_location = "all-mias/mdb{}.pgm".format(image_number)
	get_texture_glcm_measurements.delay(image_number, image_file_location)