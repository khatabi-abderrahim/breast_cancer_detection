from PCA.matrix_creation import MatrixCreation

class PCAComponentsInterpretation():
	"""
	Interpretation of the PCA results.
	"""
	def eigen_values_interpretation(self, eigen_values):
		"""
		You can use the size of the eigenvalue to determine the number of principal
		components. Retain the principal components with the largest eigenvalues. For
		example, using the Kaiser criterion, you use only the principal components with
		eigenvalues that are greater than 1.

		Arguments:
			eigen_vectors (2D array): The eigen vectors from the values

		Returns:
			principal_components (list): The principal compon
		"""
		principal_components = []

		for column in range(0,len(eigen_values)-1):
			if eigen_values[column] > 1:
				principal_components.append(MatrixCreation().matrix_labels().get(column))

		return principal_components