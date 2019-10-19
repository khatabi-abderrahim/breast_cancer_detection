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

	def make_predictions(self, label_train):
		"""
		Make predictions of one of the labels using the Logistic Regression
		classifier algorithm.

		Returns:
			label_prediction (array): The predicted results of the given label
		"""
		logistic_regresion_classifier = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')
		logistic_regresion_classifier.fit(self.data_train, label_train) 
			
		label_prediction = logistic_regresion_classifier.predict(self.data_test)

		return label_prediction

	def join_predictions(self):
		"""
		Join the the predictions of all labels

		Returns:
			label_prediction (matrix): The predicted results of every label from
									   the data set.
		"""
		label_prediction = numpy.zeros(shape=self.label_test.shape)

		for column in range(0, self.label_train.shape[1]-1):
			label_prediction[:,column] = self.make_predictions(self.label_train[:,column])

		return label_prediction