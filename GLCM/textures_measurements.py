import math

"""
They are Energy, Entropy, Contrast, Correlation, and  Homogeneity. Energy
returns the sum  of  squared elements in the GLCM and the range will be in
[0, 1]. Entropy measures the randomness  of  intensity  distribution.
Correlation measure of  image  linearity, and Homogeneity Returns a value that
measures the closeness of the distribution of elements in the GLCM to the GLCM
diagonal and range will be in [0 1].
"""

class texture_measurements():
	def contrast_group_measurements(self, glcm_percentage_matrix, pixel_set):
		"""
		Get the contrast measurements of the image from the glcm percentage matrix.
		Contrast measures the  amount  of local  variation  in  the  image.
		
		Args:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
			pixel_set (array): An array with the set of pixels in the image

		Returns:
			contrast (number): The contrast probability level of the image
			dissimilarity (number): The dissimilarity probability level of the image
			homogeneity (number): The homogeneity probability level of the image
		"""
		contrast = 0
		dissimilarity = 0
		homogeneity = 0
		
		for reference in pixel_set:
			for neighbour in pixel_set:
				contrast += glcm_percentage_matrix[reference][neighbour] * math.pow((pixel_set[reference]-pixel_set[neighbour]),2)
				dissimilarity += glcm_percentage_matrix[reference][neighbour] * abs(pixel_set[reference]-pixel_set[neighbour])
				homogeneity += float(glcm_percentage_matrix[reference][neighbour]) / float(1 + math.pow((pixel_set[reference]-pixel_set[neighbour]),2))

		return contrast, dissimilarity, homogeneity

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
