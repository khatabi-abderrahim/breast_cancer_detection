import cv2
import numpy as np
from GLCM.pixel_matrix import *

"""
Script to gextract the features from the image
"""

# image
image = cv2.imread('all-mias/mdb001.pgm',0)
image_shape = image.shape
image_rows = image_shape[0]
image_columns = image_shape[1]

example_image = np.array([[0, 0, 1, 1],
						  [0, 0, 1, 1],
						  [0, 2, 2, 2],
						  [2, 2, 3, 3],
				])

pixels = number_of_pixels(example_image)
print(pixels)

first_pixels = pixels[:4]

c_matrix = co_ocurrency_matrix_horizontal()

new_matrix = c_matrix.horizontal_relationship(example_image, pixels)
print (new_matrix)