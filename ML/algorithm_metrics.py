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