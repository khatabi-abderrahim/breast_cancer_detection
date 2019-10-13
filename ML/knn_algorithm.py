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
			errosrs (array): An array with all the obtained erros.
		"""
		errors = []
		
		# Calculating error for K values between 1 and 40
		for neighbors in range(1, 51):
		    knn_classifier = KNeighborsClassifier(n_neighbors=neighbors)
		    knn_classifier.fit(training_and_test_data[0], training_and_test_data[2])
		    predict_labels = knn_classifier.predict(training_and_test_data[1])
		    # Calculate the mean when the predicte data is not correct
		    errors.append(numpy.mean(predict_labels != training_and_test_data[3]))

		return errors