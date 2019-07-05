import numpy as np

def number_of_pixels(image):
	"""
	Get the number of the different pixels in the given image
	
	Args:
		image (array): The image to get the diferent pixels

	Returns:
		pixels (Array): The different pixels in the image
	"""
	pixels = list(set(image.flat))
	
	return pixels

def create_matrix(pixels):
	"""
	Create an empty co-occurrence matrix of the chosen image
	
	Args:
		pixel (array): The image to get the diferent pixels

	Returns:
		co_ocurrence_matrix (matrix): An empty matrix with the size of the number
									  of pixels of the image
	"""
	number_of_pixels = len(pixels)
	co_ocurrence_matrix = np.zeros(shape=(number_of_pixels,number_of_pixels))
	
	return co_ocurrence_matrix

def transpose_matrix(matrix):	
	"""
	Get the transpose of a given matrix
	
	Args:
		matrix (array): The matrix to be transposed

	Returns:
		transposed_matrix (array): The transposed matrix to be transposed
	"""
	transposed_matrix = np.zeros(shape=matrix.shape)

	for column in range(0,matrix.shape[1]):
		transposed_matrix[column,:] = matrix[:,column]

	return transposed_matrix

def pixel_relationship_diagonal(image, reference, neighbour):
	"""
	Get the number of times the relationship between the given reference pixel and
	neighnpur pixel occur in the image
	
	Args:
		image (array): The image where the number of relationships will be obtained
		image_rows (number): Number of rows in the image
		image_columns (number): Number of columns in the image
		reference (number): The reference pixel
		neighbour (number): The neighbour pixel

	Returns:
		count (number): The number of times the relationship happens in the given image
	"""
	image_rows = image.shape[0]
	image_columns = image.shape[1]
	count = 0
	for row in range(1, image_rows-1):
		for column in range(1, image_columns-1):
			if image[row][column] == reference and image[row+1][column+1] == neighbour :
				count += 1
	return count
