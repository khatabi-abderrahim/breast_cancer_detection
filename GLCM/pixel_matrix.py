import numpy
import cv2
from skimage import feature
from GLCM.GLCM_helper_functions import string_array_to_int_array, reduce_images
from helper_functions import read_text_files, write_text_files

class CoOcurrencyMatrixVertical():
	"""
	A grey level co-occurrence matrix is a histogram of co-occurring greyscale values
	at a given offset over an image.
	"""

	def vertical_relationship_probabilities(self, image_number, image_file_location, pixels_file_location):
		"""
		Get the probability of the vertical relationship of grey pixels in the image
		
		Args:
			image_location (string): The location of image to be read and converted
									 into a 2D array
			pixel_file_location (string): The location of the image pixels to be read
										  and converted into an array 

		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		# Reads the image from the fila
		image = cv2.imread(image_file_location, 0)
		image = reduce_images(image)

		glcm_percentage_matrix = feature.greycomatrix(image=image, distances=[1],
			angles=[0, numpy.pi/4, numpy.pi/2, 3*numpy.pi/4],
				normed=True, symmetric=True, levels=255)
		
		#write_text_files("GLCM/matrix/percentage_matrix_image{}".format(image_number), glcm_percentage_matrix)
		numpy.savetxt("GLCM/matrix/glcm_percentage_matrix_image{}_1.txt".format(image_number), glcm_percentage_matrix[:, :, 0, 0])

		return "GLCM/matrix/percentage_matrix_image{}".format(image_number)
