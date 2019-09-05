import numpy

def calculate_matrix_transpose(matrix):
	"""
	Receives a matrix and returns it's transpose

	Args:
		matrix (array): The matrix that will be transposed

	Returns:
		transposed_matrix (array): The transposed matrix
	"""
	matrix_rows = matrix.shape[0]
	matrix_columns = matrix.shape[1]

	transposed_matrix = numpy.zeros(shape=(matrix_columns,matrix_rows))

	for rows in range(0,transposed_matrix.shape[0]):
		transposed_matrix[rows,:] = matrix[:,rows]

	return transposed_matrix