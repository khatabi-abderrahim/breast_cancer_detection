import numpy
from sklearn import svm
from PCA.matrix_creation import MatrixCreation
from ML.prepare_data import PrepareData

class SvmAlgorithm():
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

	def make_predictions(self):
		"""
		Make predictions of one of the labels.

		Returns:
			label_prediction (array): The predicted results
		"""
		svm_classifier = svm.SVC(gamma='scale', decision_function_shape='ovo')
		svm_classifier.fit(self.data_train, self.label_train[:,0]) 
			
		label_prediction = svm_classifier.predict(self.data_test)

		return label_prediction	