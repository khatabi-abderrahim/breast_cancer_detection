import numpy
from sklearn.metrics import multilabel_confusion_matrix
from PCA.matrix_creation import MatrixCreation
from ML.prepare_data import PrepareData

class ConfusionMatrix():
	"""
	It's a specific table layout that allows visualization of the performance
	of an algorithm
	"""
	def __init__(self, predicted_results):
		"""
		Constructor method that initialices the result labels used to train the
		algorithm and the actual results.
		"""
		label_matrix = MatrixCreation().create_full_matrix()[:,range(24,36)]

		self.label_test = PrepareData().create_training_and_test_data_sets(label_matrix=label_matrix)[3]
		self.predicted_results = predicted_results
		self.labels =  ['Fatty', 'Fatty-glandular', 'Dense-glandular', 'Calcification', 'Well-defined/circumscribed masses',
						'Spiculated masses', 'Other, ill-defined masses', 'Architectural distortion', 'Asymmetry', 'Normal',
                		'Benign', 'Malignant']

	def create_confusion_matrix(self):
		"""
		Creates the Confusion Matrix for each of the labels.
		
		[0,0]: True Negatives - [0,1]: False Positives
		[1,0]: False Negatives - [1,1]: True Positives
		
		Args:
			true_results (matrix): True results obtained from the all-mias dataset
			predicted_results (matris): The predicted results obtained from the
										classification algorithm

		Returns:
			normalized_confusion_matrix (matrix): A Multidimensional array conaining the
											      normalized confusion matrix of every label. 
		"""
		labels_confusion_matrixes = multilabel_confusion_matrix(self.label_test, self.predicted_results)

		return labels_confusion_matrixes

	def calculate_sensitivity(self):
		"""
		Calculate the sensitivity of the predicted labels in the algorithm using the
		confusion matrix. It measures the proportion of actual positives that are
		correctly identified as such.
		True Positive / (True positive + False Negative)

		Returns:
			sensitivity (dictionary): Maps the lable with its calculated sensitivity 
		"""
		sensitivity = {}
		labels = self.labels

		for index,label in enumerate(labels):
			sensitivity[label] = (self.create_confusion_matrix()[index][1][1]/(self.create_confusion_matrix()[index][1][1]+ self.create_confusion_matrix()[index][1][0]))

		return sensitivity

	def calculate_specificity(self):
		"""
		Calculate the specificity of the predicted labels in the algorithm using the
		confusion matrix. It measures the proportion of actual negatives that are
		correctly identified as such.
		True Negative / (True Negative + False Positive)

		Returns:
			specificity (dictionary): Maps the lable with its calculated specificity
		"""
		specificity = {}
		labels = self.labels

		for index,label in enumerate(labels):
			specificity[label] = (self.create_confusion_matrix()[index][0][0]/(self.create_confusion_matrix()[index][0][0]+ self.create_confusion_matrix()[index][0][1]))

		return specificity

	def calculate_precision(self):
		"""
		Calculate the precision of the predicted labels in the algorithm using the
		confusion matrix. The proportions of positive results that are true positives.
		True Positive / (True Positive  + False Positive)

		Returns:
			precision (dictionary): Maps the lable with its calculated precision
		"""
		precision = {}
		labels = self.labels

		for index,label in enumerate(labels):
			precision[label] = (self.create_confusion_matrix()[index][1][1]/(self.create_confusion_matrix()[index][1][1]+ self.create_confusion_matrix()[index][0][1]))

		return precision