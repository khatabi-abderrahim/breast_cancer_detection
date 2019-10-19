import numpy
import random
from sklearn.model_selection import train_test_split
from PCA.matrix_creation import MatrixCreation

class PrepareData():
	def __init__(self):
		"""
		Constructor method that initialices the labels of the principal components.
		"""
		self.principal_components = ['contrast right', 'contrast left', 'contrast up',
		'contrast down', 'energy right', 'energy left', 'energy up', 'energy down',
		'dissimilarity right', 'dissimilarity left', 'dissimilarity up',
		'dissimilarity down', 'homogeneity right', 'homogeneity left', 'homogeneity up',
		'homogeneity down', 'correlation right', 'correlation left']
		self.texture_matrix = self.prepare_texture_matrix()
		self.labels_matrix = self.balance_clases()[:,range(24,36)]

	def balance_clases(self):
		"""
		Balance the classes so there is a 1:1 proportion of normal breast images and
		abnormal breast images. Selects from the matrix the images that are normal to
		randomly delete a portion of those images.

		Returns:
			full_matrix (matrix): A matrix with every component and label, and a 1:1
								  proportion of normal and abnormal images.
		"""
		full_matrix = MatrixCreation().create_full_matrix()
		
		normal_images = []

		for row_index, row_elements in enumerate(full_matrix):
			if row_elements[33] == 1:
				normal_images.append(row_index)

		full_matrix = numpy.delete(arr=full_matrix,obj=random.sample(normal_images,len(normal_images)-(full_matrix.shape[0]-len(normal_images))), axis=0)
		
		return full_matrix

	def prepare_texture_matrix(self):
		"""
		Creates the matrix using only the principal components chosen from the PCA

		Args:
			principal_components (array): A string array containing the principal components

		Returns:
			texture_matrix (matrix): A matrix with the principal textures to be analyzed in
									 the machine learning algorithm.
		"""
		full_matrix = self.balance_clases()
		labels = MatrixCreation().independent_variable_labels()

		texture_matrix = full_matrix[:,range(0,24)]
		
		columns_to_be_deleted = []

		for key, label in labels.items():
			if label not in self.principal_components:
				columns_to_be_deleted.append(key)

		texture_matrix = numpy.delete(texture_matrix,columns_to_be_deleted,axis=1)

		return texture_matrix

	def create_training_and_test_data_sets(self):
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
		data_train, data_test, label_train, label_test = train_test_split(self.texture_matrix, self.labels_matrix , test_size=0.20)

		return data_train, data_test, label_train, label_test