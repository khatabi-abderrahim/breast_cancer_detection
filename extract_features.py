import cv2
import numpy as np
from GLCM.pixel_matrix import *
from GLCM.textures_measurements import *

"""
Script to extract the features from the image
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

c_matrix = co_ocurrency_matrix_vertical()

new_matrix = c_matrix.vertical_relationship(example_image, pixels)
print (new_matrix)

glcm_percentage_matrix = c_matrix.vertical_relationship_probabilities(new_matrix)
print(glcm_percentage_matrix)

measurements = texture_measurements()
contrast = measurements.contrast_group_measurements(glcm_percentage_matrix, pixels)

# Create a text file to write the GLCM results
data_file = open("Results/GLCM_results.txt","w+")
data_file.write("contrast: {} - dissimilarity: {} - homogeneity: {}".format(contrast[0], contrast[1], contrast[2]))