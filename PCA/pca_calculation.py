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
	def calculate_standardized_variables(self, glcm_measurements):
		"""
		First unify each variable from the matrix

		Args:
			glcm_measurements (array): The GLCM measurements data

		Returns:
			unified_measurements (array): The unified GLCM measurements 
		"""
		glcm_measurements = numpy.array(glcm_measurements)

		standardized_variables = numpy.zeros(shape=(glcm_measurements.shape))

		for row in range(0,glcm_measurements.shape[0]):
			for column in range(0,glcm_measurements.shape[1]):
				standardized_variables[row][column] = (glcm_measurements[row][column] - round(glcm_measurements[:,column].mean(),5))/round(glcm_measurements[:,column].std(ddof=1),5)

		standardized_variables = numpy.round(standardized_variables,3)

		return standardized_variables

	def calculate_correlation_matrix(self, unified_measurements):
		"""
		Multiplies the unified variables matrix by it's transpose

		Args:
			unified_measurements (array): The unified GLCM measurements

		Returns:
			correlation_matrix (array): The resultant matrix multiplication
		"""
		correlation_matrix = numpy.dot(unified_measurements.transpose(),unified_measurements)
		correlation_matrix = numpy.round(correlation_matrix,3)

		return correlation_matrix

	def calculate_singular_value_decomposition(self, unified_measurements):
		"""
		It is the generalization of the eigendecomposition of a positive normal matrix

		Arguments:
			unified_measurements (matrix): 

		Returns:
			unitary_values (matrix): Matrix with the unitary arrays (P)
			eigen_values (matrix):  Matrix with the singular values (D)
			eigen_vectors (matrix):  Matrix with the singular vectors (Q)
		"""

		unitary_values, eigen_values, eigen_vectors = numpy.linalg.svd(unified_measurements, full_matrices=True)

		unitary_values = numpy.round(unitary_values,3)
		eigen_values = numpy.round(eigen_values,3)
		eigen_vectors = numpy.round(eigen_vectors,3)
		
		return unitary_values,eigen_values, eigen_vectors

	def calculate_variance_vector(self, eigen_values, number_of_rows):
		"""
		Calculate the variance vector

		Arguments:
			eigen_values (matrix):  Matrix with the singular values (D)
			number_of_rows (number): The number of rows of the data matrix

		Resutrns:
			variance_vector (matrix): 
		"""

		variance_vector = eigen_values/numpy.sqrt(number_of_rows-1)
		variance_vector = numpy.round(variance_vector,5)

		return variance_vector