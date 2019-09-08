import cv2
import numpy
from GLCM.pixel_matrix import number_of_pixels
from GLCM.textures_measurements import *
from tasks import get_vertical_glcm_matrix

"""
Script to extract the features from the image
"""

# Get the number of each of the dataset image
number_of_pixels()

"""
Call the function that will delegate the GLCM vertical relationship
calculations in an asynchronous way.
"""
for number in range(1,4):
	image_file_location = "all-mias/mdb{}.pgm".format(number)
	pixels_file_location = "GLCM/pixels/mdb{}.txt".format(number)
	get_vertical_glcm_matrix.delay(image_file_location, pixels_file_location)


"""
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
"""