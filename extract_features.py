import cv2
import numpy
from tasks import get_vertical_glcm_matrix

"""
Script to extract the features from the image
"""
"""
Call the function that will delegate the GLCM vertical relationship
calculations in an asynchronous way.
"""
image_number = 1

image_file_location = "all-mias/mdb{}.pgm".format(image_number)
get_vertical_glcm_matrix.delay(image_number, image_file_location)