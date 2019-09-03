import numpy
import pca_math

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

		Args:
			glcm_measurements (array): The GLCM measurements data

		Returns:
			unified_measurements (array): The unified GLCM measurements 
		"""
		glcm_measurements = numpy.array(glcm_measurements)
		unified_measurements = numpy.empty(glcm_measurements.shape)
		
		for value in range(0,glcm_measurements.size-1):
			unified_measurements[value] = (glcm_measurements[value] - round(glcm_measurements.mean(),4))/round(glcm_measurements.std(),4)

		return unified_measurements

	def multiply_variables_transpose(self, unified_measurements):
		"""
		Multiplies the unified variables matrix by it's transpose

		Args:
			unified_measurements (array): The unified GLCM measurements

		Returns:
			matrix_a (array): The resultant matrix multiplication
		"""
		matrix_a = numpy.empty(unified_measurements.shape)
		transposed_unified_measurements = pca_math.matrix_transpose(unified_measurements)

		matrix_a = unified_measurements * transposed_unified_measurements

		return matrix_a