import numpy

class  pca_matrix_creation():
	"""
	Create the PCA matrix with the GLCM variables of every image in the dataset.
	"""
	def read_text_file(self):
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

class pca_calculation():
	"""
	Calculate the principal components from the GLCM measurements to validate wich
	one of them will be able to predict if the image has a malformation
	"""
	def unify_variables(self, glcm_measurements):
		"""
		First unify each variable from the matrix
		"""
		glcm_measurements = numpy.array(glcm_measurements)
		
		for value in range(0,glcm_measurements.size-1):
			glcm_measurements[value] = (glcm_measurements[value] - round(glcm_measurements.mean(),4))/round(glcm_measurements.std(),4)

		return glcm_measurements