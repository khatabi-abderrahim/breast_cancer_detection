import numpy
from sklearn import svm
from PCA.matrix_creation import MatrixCreation
from ML.prepare_data import PrepareData

class LogisticRegresionAlgorithm():
	def __init__(self):
		"""
		Constructor method that keeps the data and labels in two sets for
		training and testing. 
		"""
		self.data_train = PrepareData().create_training_and_test_data_sets()[0]
		self.data_test = PrepareData().create_training_and_test_data_sets()[1]
		self.label_train = PrepareData().create_training_and_test_data_sets()[2]
		self.label_test = PrepareData().create_training_and_test_data_sets()[3]

