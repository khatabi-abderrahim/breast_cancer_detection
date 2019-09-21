import numpy
import cv2
from skimage import feature
from GLCM.GLCM_helper_functions import reduce_images

class CoOcurrencyMatrix():
	"""
	A grey level co-occurrence matrix is a histogram of co-occurring greyscale values
	at a given offset over an image.
	"""

	def relationship_probabilities(self, image_file_location):
		"""
		Get the probability of the vertical relationship of grey pixels in the image
		
		Args:
			image_location (string): The location of image to be read and converted
									 into a 2D array
		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		# Reads the image from the fila
		image = cv2.imread(image_file_location, 0)

		glcm_percentage_matrix = feature.greycomatrix(image=image, distances=[1],
			angles=[0, numpy.pi/4, numpy.pi/2, 3*numpy.pi/4],
				normed=True, symmetric=True, levels=255)

		return glcm_percentage_matrix
