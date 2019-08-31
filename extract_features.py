import cv2
import numpy
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
example_image = numpy.array([[0, 0, 1, 1],
						  [0, 0, 1, 1],
						  [0, 2, 2, 2],
						  [2, 2, 3, 3],
				])

pixels = number_of_pixels(example_image)

first_pixels = pixels[:4]

# Calculate the vertical matrix
vertical_matrix_object = co_ocurrency_matrix_vertical()

vertical_matrix = vertical_matrix_object.vertical_relationship(example_image, pixels)

glcm_vertical_percentage_matrix = vertical_matrix_object.vertical_relationship_probabilities(vertical_matrix)

# Calculate the vertical GLCM texture measurements
vertical_measurements_object = texture_measurements()
vertical_contrast = vertical_measurements_object.contrast_group_measurements(glcm_vertical_percentage_matrix, pixels)
vertical_energy = vertical_measurements_object.energy_measurements(glcm_vertical_percentage_matrix, pixels)

# Calculate the horizontal matrix
horizontal_matrix_object = co_ocurrency_matrix_horizontal()

horizontal_matrix = horizontal_matrix_object.horizontal_relationship(example_image, pixels)

glcm_horizontal_percentage_matrix = horizontal_matrix_object.horizontal_relationship_probabilities(horizontal_matrix)

# Calculate the horizontal GLCM texture measurements
horizontal_measurements_object = texture_measurements()
horizontal_contrast = horizontal_measurements_object.contrast_group_measurements(glcm_horizontal_percentage_matrix, pixels)

# Create a text file to write the GLCM results
data_file = open("Results/GLCM_results.txt","a+")
data_file.write("{}\n{}\n{}\n{}\n".format(vertical_contrast[0], vertical_contrast[1], vertical_contrast[2],vertical_energy))
data_file.write("{}\n{}\n{}\n".format(horizontal_contrast[0], horizontal_contrast[1], horizontal_contrast[2]))