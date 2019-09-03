import numpy

def matrix_transpose(matrix):
	"""
	Receives a matrix and returns it's transpose

	Args:
		matrix (array): The matrix that will be transposed

	Returns:
		transposed_matrix (array): The transposed matrix
	"""
	transposed_matrix = numpy.empty(matrix.shape)

	for file in range(0,matrix.shape[0]):
		transposed_matrix[file,:] = matrix[:,file]

	return transposed_matrix