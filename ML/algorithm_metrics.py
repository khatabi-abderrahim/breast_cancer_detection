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

		for index,label in enumerate(self.labels):
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

		for index,label in enumerate(self.labels):
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

		for index,label in enumerate(self.labels):
			precision[label] = (self.create_confusion_matrix()[index][1][1]/(self.create_confusion_matrix()[index][1][1]+ self.create_confusion_matrix()[index][0][1]))

		return precision

	def calculate_negative_predictive_value(self):
		"""
		Calculate the negative predictive value of the predicted labels in the algorithm
		using the confusion matrix. The proportions of negative results that are
		true negative.
		True Negative / (True Negative  + False Negative)

		Returns:
			precision (dictionary): Maps the lable with its calculated precision
		"""
		negative_predictive_value = {}

		for index,label in enumerate(self.labels):
			negative_predictive_value[label] = (self.create_confusion_matrix()[index][0][0]/(self.create_confusion_matrix()[index][0][0]+ self.create_confusion_matrix()[index][1][0]))

		return negative_predictive_value

	def calculate_false_negative_rate(self):
		"""
		Calculate the false negative rate value of the predicted labels in the algorithm
		using the confusion matrix. A failure to reject a false null hypothesis. It is
		also known as type II error. This type of error leads to the conclusion that a
		supposed effect or relationship does not exists when in fact it does. An example
		is when a blood test fails to detect the disease it was designed to detect, in a
		patient who really has the disease.
		False Negative / (False Negative  + True Positive)

		Returns:
			false_negative_rate (dictionary): Maps the lable with its false_negative_rate
		"""
		false_negative_rate = {}

		for index,label in enumerate(self.labels):
			false_negative_rate[label] = (self.create_confusion_matrix()[index][1][0]/(self.create_confusion_matrix()[index][1][0]+ self.create_confusion_matrix()[index][1][1]))

		return false_negative_rate

	def calculate_false_positive_rate(self):
		"""
    	Calculate the false negative rate value of the predicted labels in the algorithm
    	using the confusion matrix. A failure to reject a true null hypothesis. It is
    	also known as type I error. This type of error leads to the conclusion that a
    	supposed effect or relationship does not exists when in fact it does. An example
    	is when a test that shows a patient has a disease when in fact the patient does
    	not have the it.
    	False Positive / (False Positive  + True Negative)

    	Returns:
    		false_positive_rate (dictionary): Maps the lable with its false_positive_rate
    	"""
		false_negative_rate = {}

		for index,label in enumerate(self.labels):
			false_negative_rate[label] = (self.create_confusion_matrix()[index][0][1]/(self.create_confusion_matrix()[index][0][1]+ self.create_confusion_matrix()[index][1][0]))

		return false_negative_rate

	def calculate_false_discovery_rate(self):
		"""
		Calculate the false discovery rate value of the predicted labels in the
		algorithm using the confusion matrix. It is the expected proportion of type I
		errors.
		False Positive / (False Positive  + True Positive)

		Returns:
			false_discovery_rate (dictionary): Maps the lable with its false_discovery_rate
		"""
		false_discovery_rate = {}

		for index,label in enumerate(self.labels):
			false_discovery_rate[label] = (self.create_confusion_matrix()[index][0][1]/(self.create_confusion_matrix()[index][0][1]+ self.create_confusion_matrix()[index][1][1]))

		return false_discovery_rate