import numpy as np

def number_of_pixels(image, image_rows, image_columns):
	"""
	Get the number of the different pixels in the given image
	
	Args:
		image (array): The image to get the diferent pixels
		image_rows (number): Number of rows in the image
		image_columns (number): Number of columns in the image

	Returns:
		pixels (Array): The different pixels in the image
	"""
	pixels = []
	for row in range(0, image_rows):
		for column in range(0, image_columns):
			if image[row][column] not in pixels:
				pixels.append(image[row][column])
	sorted(pixels)
	
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