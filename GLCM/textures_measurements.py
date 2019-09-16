from skimage import feature
import numpy
import math
from GLCM.pixel_matrix import CoOcurrencyMatrix

class TextureMeasurements():
	"""
	They are Energy, Entropy, Contrast, Correlation, and  Homogeneity. Energy
	returns the sum  of  squared elements in the GLCM and the range will be in
	[0, 1]. Entropy measures the randomness  of  intensity  distribution.
	Correlation measure of  image  linearity, and Homogeneity Returns a value that
	measures the closeness of the distribution of elements in the GLCM to the GLCM
	diagonal and range will be in [0 1].
	"""

	def contrast_measurements(self, image_number, image_file_location):
		"""
		Get the contrast measurements of the image from the glcm percentage matrix.
		Contrast measures the  amount  of local  variation  in  the  image.
		feature.greycoprops(prop='contrast'): The tecture property to be 
											  calculated from the GLCM matrix
		
		Args:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
			image_number (number): A number that identifies the image to be analyzed

		Returns:
			(string): The location of where the contrast information 
					  of the matrix will be saved
		"""
		glcm_percentage_matrix = CoOcurrencyMatrix().relationship_probabilities(image_file_location)
		contrast = feature.greycoprops(glcm_percentage_matrix, prop='contrast')
		numpy.savetxt("GLCM/matrix/contrast_mdb{}.txt".format(image_number), contrast)

		return "GLCM/matrix/contrast_mdb{}.txt".format(image_number)

	def energy_measurements(self, glcm_percentage_matrix, pixel_set):
		"""
		Get the energy measurements of the image from the glcm percentage matrix.
		
		Args:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
			pixel_set (array): An array with the set of pixels in the image

		Returns:
			energy (number): The contrast probability level of the image
		"""
		energy = 0

		for reference in pixel_set:
			for neighbour in pixel_set:
				energy += math.pow(glcm_percentage_matrix[reference][neighbour],2)

		return energy
