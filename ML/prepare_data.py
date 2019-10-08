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

	def create_training_and_test_data_sets(self, label_matrix):
		"""
		Splits all the result data and the variable data into two sets: training (80 %
		of the data) and testing (20 % of the data).

		Args:
			label_matrix (matrix): The labels results gotten from the all-mias dataset.

		Returns:
			data_train (matrix): The data that will be used to train the algorithm.
			data_test (matrix): The data that will be used to test the algorithm.
			label_train (matrix): The result data that will be used to test the algorithm.
			label_test (matrix): The result data that will be compared to the predicted data
								 to get how correct is the algorithm.
		"""
		principal_components = ['contrast right', 'contrast left', 'contrast up',
		'contrast down', 'energy right', 'energy left', 'energy up', 'energy down',
		'dissimilarity right', 'dissimilarity left', 'dissimilarity up',
		'dissimilarity down', 'homogeneity right', 'homogeneity left', 'homogeneity up',
		'homogeneity down', 'correlation right', 'correlation left']


		data_train, data_test, label_train, label_test = train_test_split(self.prepare_texture_matrix(principal_components=principal_components), label_matrix, test_size=0.20)

		return data_train, data_test, label_train, label_test