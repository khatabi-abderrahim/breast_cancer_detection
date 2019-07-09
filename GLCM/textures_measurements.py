import math

class texture_measurements():
	def contrast_group_measurements(self, glcm_percentage_matrix, pixel_set):
		"""
		Get the contrast measurements of the image from the glcm percentage matrix
		
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