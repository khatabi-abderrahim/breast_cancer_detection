class  pca_matrix_creation():
	"""
	Create the PCA matrix with the GLCM variables of every image in the dataset.
	"""
	def read_text_file():
		"""
		Extracts the GLCM measurments from the file and creates an array with the data

		Returns:
			glcm_measurements (array): The GLCM measurements data
		"""
		text_file_lines = open("Results/GLCM_results.txt","r").readlines()

		glcm_measurements = []

		for element in text_file_lines:
			element = element.split('\n')
			element = float(element[0])
			glcm_measurements.append(element)

		return glcm_measurements