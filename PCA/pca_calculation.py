import numpy
from sklearn.preprocessing import StandardScaler
from PCA.matrix_creation import MatrixCreation

class PCACalculation():
	"""
	Calculate the principal components from the GLCM measurements to validate wich
	one of them will be able to predict if the image has a malformation
	"""
	def calculate_standardized_variables(self, glcm_texture_measurements):
		"""
		First unify each variable from the matrix

		Args:
			glcm_measurements (array): The GLCM measurements data

		Returns:
			standardized_measurements (array): The unified GLCM measurements 
		"""
		standardized_variables = numpy.zeros(shape=(glcm_texture_measurements.shape))
		
		for row in range(0,glcm_texture_measurements.shape[0]):
			for column in range(0,glcm_texture_measurements.shape[1]):
				standardized_variables[row][column] = (glcm_texture_measurements[row][column] - round(glcm_texture_measurements[:,column].mean(),5))/round(glcm_texture_measurements[:,column].std(ddof=1),5)

		standardized_variables = numpy.round(standardized_variables,3)

		return standardized_variables

	def calculate_singular_value_decomposition(self, standardized_variables):
		"""
		It is the generalization of the eigendecomposition of a positive normal matrix

		Arguments:
			unified_measurements (matrix): 

		Returns:
			unitary_values (matrix): Matrix with the unitary arrays (P)
			eigen_values (matrix):  Matrix with the singular values (D)
			eigen_vectors (matrix):  Matrix with the singular vectors (Q)
		"""

		unitary_values, eigen_values, eigen_vectors = numpy.linalg.svd(standardized_variables)

		unitary_values = numpy.round(unitary_values,3)
		eigen_values = numpy.round(eigen_values,3)
		eigen_vectors = numpy.round(eigen_vectors,3)
		
		return unitary_values, eigen_values, eigen_vectors

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

	def calculate_loadings(self, variance_vectors, eigen_vectors):
		"""
		Calculate loadings to visualice how variabels group.

		Arguments:
			variance_vector (matrix):

		Returns:
			loadings (matrix):
		"""
		loadings = numpy.zeros(shape=(eigen_vectors.shape))

		for column in range(0,len(variance_vectors)-1):
			loadings[:,column] = numpy.round((eigen_vectors[:,column] * variance_vectors[column]),4)

		return loadings

	def calculate_scores(self, standardized_variables, eigen_vectors):
		"""
		Calculate scores

		Arguments:
			standardized_measurements (array): The unified GLCM measurements (A)
			eigen_vectors (matrix):  Matrix with the singular vectors (Q)
		
		Returns:
			score_values (matrix):
		"""
		#scores_values = numpy.dot(standardized_variables,eigen_vectors)
		scores_values = numpy.matmul(standardized_variables,eigen_vectors)
		
		return scores_values

	def calculate_square_cosines(self, loadings):
		"""
		Calculate square cosines

		Arguments:
			loadings (matrix)

		Returns:
			square_cosines (matrix)
		"""
		square_cosines = numpy.square(loadings)

		return square_cosines

	def calculate_principal_components(self, glcm_texture_measurements):
		"""
		Calculate the principal components of the image textures.

		Arguments:
			glcm_texture_measurements (2D array): The matrix of the GLCM testure measurements.
											   Every row is an image and every column is a texture.
		Returns:
			scores (2D array):
		"""
		standard_values = self.calculate_standardized_variables(glcm_texture_measurements=glcm_texture_measurements)
		single_value_decomposition = self.calculate_singular_value_decomposition(standardized_variables=standard_values)
		variance_vectors = self.calculate_variance_vector(eigen_values=single_value_decomposition[1], number_of_rows=glcm_texture_measurements.shape[0])
		loadings = self.calculate_loadings(variance_vectors=variance_vectors, eigen_vectors=single_value_decomposition[2])
		scores = self.calculate_scores(standardized_variables=standard_values , eigen_vectors=single_value_decomposition[2])
		square_cosines = self.calculate_square_cosines(loadings=loadings)

		return square_cosines
