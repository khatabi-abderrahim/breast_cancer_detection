import numpy
from sklearn.model_selection import train_test_split
from PCA.matrix_creation import MatrixCreation

class PrepareData():
	def prepare_texture_matrix(self, principal_components):
		"""
		Creates the matrix using only the principal components chosen from the PCA

		Args:
			principal_components (array): A string array containing the principal components

		Returns:
			texture_matrix (matrix): A matrix with the principal textures to be analyzed in
									 the machine learning algorithm.
		"""
		full_matrix = MatrixCreation().create_full_matrix()
		labels = MatrixCreation().independent_variable_labels()

		texture_matrix = full_matrix[:,range(0,24)]
		
		columns_to_be_deleted = []

		for key, label in labels.items():
			if label not in principal_components:
				columns_to_be_deleted.append(key)

		texture_matrix = numpy.delete(texture_matrix,columns_to_be_deleted,axis=1)

		return texture_matrix

