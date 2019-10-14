import numpy
from sklearn import svm
from PCA.matrix_creation import MatrixCreation
from ML.prepare_data import PrepareData

class SvmAlgorithm(self):
		def __init__(self):
		"""
		Constructor method that keeps the data and labels in two sets for
		training and testing. 
		"""
		
		label_matrix = MatrixCreation().create_full_matrix()[:,range(24,36)]

		self.data_train = PrepareData().create_training_and_test_data_sets(label_matrix=label_matrix)[0]
		self.data_test = PrepareData().create_training_and_test_data_sets(label_matrix=label_matrix)[1]
		self.label_train = PrepareData().create_training_and_test_data_sets(label_matrix=label_matrix)[2]
		self.label_test = PrepareData().create_training_and_test_data_sets(label_matrix=label_matrix)[3]