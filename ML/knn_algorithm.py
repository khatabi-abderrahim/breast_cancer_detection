from sklearn.neighbors import KNeighborsClassifier
import numpy

class KnnAlgorithm():
	def calculate_neighbors_errors(self, training_and_test_data):
		"""
		Calculates the errors from the knn neighbours in range from one to fifty-one.
		
		Args:
			training_and_test_data (Tuple):
				training_and_test_data[0]: data_train
				training_and_test_data[1]: data_test
				training_and_test_data[2]: label_train
				training_and_test_data[3]: label_test

		Returns:
			errors (dictionary): An array with that maps all the obtained erros with the
								  number of neighbours.
		"""
		errors = {}
		
		# Calculating error for K values between 1 and 40
		for neighbors in range(1, 51):
		    knn_classifier = KNeighborsClassifier(n_neighbors=neighbors)
		    knn_classifier.fit(training_and_test_data[0], training_and_test_data[2])
		    predict_labels = knn_classifier.predict(training_and_test_data[1])
		    # Calculate the mean when the predicte data is not correct
		    errors[neighbors] = numpy.mean(predict_labels != training_and_test_data[3])

		return errors

	def calculate_minimum_error(self, training_and_test_data):
		"""
		Get the neighbour with that gets the smallest error
		
		Args:
			training_and_test_data (Tuple)

		Returns:
			best_neighbor (number): the neighbour with that gets the smallest error
		"""
		errors = self.calculate_neighbors_errors(training_and_test_data)
		smallest_error = 1
		best_neighbor = 0

		for errors_key, errors_value in errors.items():
			if errors_value < smallest_error :
				best_neighbor = errors_key

		return best_neighbor