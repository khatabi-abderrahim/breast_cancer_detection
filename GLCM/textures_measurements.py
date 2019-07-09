import math

class texture_measurements():
	def contrast_measure(self, glcm_percentage_matrix, pixel_set):
		"""
		Get the contrast measure of the image from the glcm percentage matrix
		
		Args:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
			pixel_set (array): An array with the set of pixels in the image

		Returns:
			contrast (array): The contrast percentage level of the image
		"""
		contrast = 0
		
		for reference in pixel_set:
			for neighbour in pixel_set:
				contrast += glcm_percentage_matrix[reference][neighbour] * math.pow((pixel_set[reference]-pixel_set[neighbour]),2)

		return contrast