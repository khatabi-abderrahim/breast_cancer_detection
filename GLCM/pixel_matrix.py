import numpy

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
	co_ocurrence_matrix = numpy.zeros(shape=(number_of_pixels,number_of_pixels))
	
	return co_ocurrence_matrix

def transpose_matrix(matrix):	
	"""
	Get the transpose of a given matrix
	
	Args:
		matrix (array): The matrix to be transposed

	Returns:
		transposed_matrix (array): The transposed matrix to be transposed
	"""
	transposed_matrix = numpy.zeros(shape=matrix.shape)

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

class co_ocurrency_matrix_vertical():
	
	def pixel_relationship_up(self, image, reference, neighbour):
		"""
		Get the number of times the relationship between the given reference pixel and
		neighnpur pixel occur in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			reference (number): The reference pixel
			neighbour (number): The neighbour pixel

		Returns:
			count (number): The number of times the relationship happens in the given image
		"""
		image_rows = image.shape[0]
		image_columns = image.shape[1]
		count = 0
		for row in range(1, image_rows):
			for column in range(0, image_columns):
				if image[row][column] == reference and image[row-1][column] == neighbour :
					count += 1
		return count

	def pixel_relationship_down(self, image, reference, neighbour):
		"""
		Get the number of times the relationship between the given reference pixel and
		neighnpur pixel occur in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			reference (number): The reference pixel
			neighbour (number): The neighbour pixel

		Returns:
			count (number): The number of times the relationship happens in the given image
		"""
		image_rows = image.shape[0]
		image_columns = image.shape[1]
		count = 0
		for row in range(0, image_rows-1):
			for column in range(0, image_columns):
				if image[row][column] == reference and image[row+1][column] == neighbour :
					count += 1
		return count

	def vertical_relationship(self, image, pixels):
		"""
		Get the vertical relationship of grey pixels with a difference of one pixel
		in the image and create the grey co-ocurrency matrix
		
		Args:
			image (array): The image where the number of relationships will be obtained
			pixels (array): An array with the set of pixels in the image

		Returns:
			matrix_up (array): The reference-neighbour relationship from south to north
			matrix_down (array): The reference-neighbour relationship from north o south
			glcm_matrix (array): The array of the relationships that happens
								 in the given image
		"""
		
		matrix_up = create_matrix(pixels)
		matrix_down = create_matrix(pixels)

		for pixel_reference in pixels:
			for pixel_neighbour in pixels:
				matrix_up[pixel_reference][pixel_neighbour] = self.pixel_relationship_up(image, pixel_reference, pixel_neighbour)
				matrix_down[pixel_reference][pixel_neighbour] = self.pixel_relationship_down(image, pixel_reference, pixel_neighbour)

		glcm_matrix = (matrix_down  + matrix_up) 

		return matrix_up, matrix_down, glcm_matrix

	def vertical_relationship_probabilities(self, glcm_matrixes):
		"""
		Get the probability of the vertical relationship of grey pixels in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			matrix (array): 

		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		
		matrix_up = glcm_matrixes[0]
		matrix_down = glcm_matrixes[1]
		glcm_matrix = glcm_matrixes[2]

		number_of_relationships = float((matrix_up.shape[0]-1)*matrix_up.shape[1]) + float((matrix_down.shape[0]-1)*matrix_down.shape[1])
		glcm_percentage_matrix = glcm_matrix * (1.0/number_of_relationships)
		glcm_percentage_matrix = numpy.around(glcm_percentage_matrix, decimals=3)

		return glcm_percentage_matrix

class co_ocurrency_matrix_horizontal():
	def pixel_relationship_right(self, image, reference, neighbour):
		"""
		Get the number of times the horizontal relationship from right to left between
		the given reference pixel and neighnpur pixel occur in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			reference (number): The reference pixel
			neighbour (number): The neighbour pixel

		Returns:
			count (number): The number of times the relationship happens in the given image
		"""
		image_rows = image.shape[0]
		image_columns = image.shape[1]
		count = 0
		for row in range(0, image_rows):
			for column in range(1, image_columns):
				if image[row][column] == reference and image[row][column-1] == neighbour :
					count += 1
		return count

	def pixel_relationship_left(self, image, reference, neighbour):
		"""
		Get the number of times the horizontal relationship from left to right between
		the given reference pixel and neighnpur pixel occur in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			reference (number): The reference pixel
			neighbour (number): The neighbour pixel

		Returns:
			count (number): The number of times the relationship happens in the given image
		"""
		image_rows = image.shape[0]
		image_columns = image.shape[1]
		count = 0
		for row in range(0, image_rows):
			for column in range(0, image_columns-1):
				if image[row][column] == reference and image[row][column+1] == neighbour :
					count += 1
		return count

	def horizontal_relationship(self, image, pixels):
		"""
		Get the horizontal relationship of grey pixels with a difference of one pixel
		in the image and create the grey co-ocurrency matrix
		
		Args:
			image (array): The image where the number of relationships will be obtained
			pixels (array): An array with the set of pixels in the image

		Returns:
			matrix_left (array): The reference-neighbour relationship from west to east
			matrix_right (array): The reference-neighbour relationship from east o west
			glcm_matrix (array): The array of the relationships that happens
								 in the given image
		"""
		
		matrix_left = create_matrix(pixels)
		matrix_right = create_matrix(pixels)

		for pixel_reference in pixels:
			for pixel_neighbour in pixels:
				matrix_left[pixel_reference][pixel_neighbour] = self.pixel_relationship_left(image, pixel_reference, pixel_neighbour)
				matrix_right[pixel_reference][pixel_neighbour] = self.pixel_relationship_right(image, pixel_reference, pixel_neighbour)

		glcm_matrix = (matrix_left + matrix_right) 

		return matrix_left, matrix_right, glcm_matrix

	def horizontal_relationship_probabilities(self, glcm_matrixes):
		"""
		Get the probability of the horizontal relationship of grey pixels in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			matrix (array): 

		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		
		matrix_left = glcm_matrixes[0]
		matrix_right = glcm_matrixes[1]
		glcm_horizontal_matrix = glcm_matrixes[2]

		number_of_relationships = float((matrix_left.shape[0]-1)*matrix_left.shape[1]) + float((matrix_right.shape[0]-1)*matrix_right.shape[1])
		print(number_of_relationships)
		glcm_percentage_matrix = glcm_horizontal_matrix * (1.0/number_of_relationships)
		glcm_percentage_matrix = numpy.around(glcm_percentage_matrix, decimals=3)

		return glcm_percentage_matrix
