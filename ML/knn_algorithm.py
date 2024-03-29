from sklearn.neighbors import KNeighborsClassifier
import numpy
from PCA.matrix_creation import MatrixCreation
from ML.prepare_data import PrepareData

class KnnAlgorithm():
	def __init__(self):
		"""
		Constructor method that keeps the data and labels in two sets for
		training and testing. 
		"""
		self.data_train = PrepareData().create_training_and_test_data_sets()[0]
		self.data_test = PrepareData().create_training_and_test_data_sets()[1]
		self.label_train = PrepareData().create_training_and_test_data_sets()[2]
		self.label_test = PrepareData().create_training_and_test_data_sets()[3]

	def calculate_neighbors_errors(self):
		"""
		Calculates the errors from the knn neighbours in range from one to fifty-one.

		Returns:
			errors (dictionary): An array with that maps all the obtained erros with the
								  number of neighbours.
		"""
		errors = {}
		
		# Calculating error for K values between 1 and 40
		for neighbors in range(1, 51):
		    knn_classifier = KNeighborsClassifier(n_neighbors=neighbors)
		    knn_classifier.fit(self.data_train, self.label_train)
		    predict_labels = knn_classifier.predict(self.data_test)
		    # Calculate the mean when the predicte data is not correct
		    errors[neighbors] = numpy.mean(predict_labels != self.label_test)

		return errors

	def calculate_minimum_error(self):
		"""
		Get the neighbour with that gets the smallest error

		Returns:
			best_neighbor (number): the neighbour with that gets the smallest error
		"""
		errors = self.calculate_neighbors_errors()
		smallest_error = 1
		best_neighbor = 0

		for errors_key, errors_value in errors.items():
			if errors_value < smallest_error :
				best_neighbor = errors_key

		return best_neighbor

	def make_predictions(self):
		"""
		Make predictions using the KNN classifier and the neighbour with the
		minimal errors.

		Returns:
			label_prediction (Matrix): The predicted labels from the knn classifier
		"""
		knn_classifier = KNeighborsClassifier(n_neighbors=self.calculate_minimum_error())
		knn_classifier.fit(self.data_train, self.label_train)

		#prediction
		label_prediction = knn_classifier.predict(self.data_test)

		return label_prediction