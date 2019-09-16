import numpy
import cv2
from skimage import feature
from GLCM.GLCM_helper_functions import string_array_to_int_array, reduce_images
from helper_functions import read_text_files, write_text_files

def number_of_pixels():
	"""
	Get the number of the different pixels from the images in the dataset and
	store them in text files

	Returns:
		None: There is no variable return in this functio, it is all stored
		in text files.
	"""
	for number in range(1,322):
		image = cv2.imread("all-mias/mdb{}.pgm".format(number),0)
		one_dimensional_image = list(cv2.imread('all-mias/mdb1.pgm',0).flatten())
		one_dimensional_image = list(set(one_dimensional_image))
		write_text_files("GLCM/pixels/mdb{}.txt".format(number), one_dimensional_image)
	
	return None

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

class CoOcurrencyMatrixVertical():
	"""
	A grey level co-occurrence matrix is a histogram of co-occurring greyscale values
	at a given offset over an image.
	"""

	def vertical_relationship_probabilities(self, image_number, image_file_location, pixels_file_location):
		"""
		Get the probability of the vertical relationship of grey pixels in the image
		
		Args:
			image_location (string): The location of image to be read and converted
									 into a 2D array
			pixel_file_location (string): The location of the image pixels to be read
										  and converted into an array 

		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		# Reads the image from the fila
		image = cv2.imread(image_file_location, 0)
		image = reduce_images(image)

		glcm_percentage_matrix = feature.greycomatrix(image=image, distances=[1],
			angles=[0, numpy.pi/4, numpy.pi/2, 3*numpy.pi/4],
				normed=True, symmetric=True, levels=255)
		
		#write_text_files("GLCM/matrix/percentage_matrix_image{}".format(image_number), glcm_percentage_matrix)
		numpy.savetxt("GLCM/matrix/glcm_percentage_matrix_image{}_1.txt".format(image_number), glcm_percentage_matrix[:, :, 0, 0])

		return "GLCM/matrix/percentage_matrix_image{}".format(image_number)

class co_ocurrency_matrix_horizontal():
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

	def horizontal_relationship_probabilities(self, image_number, image_file_location, pixels_file_location):
		"""
		Get the probability of the horizontal relationship of grey pixels in the image
		
		Args:
			image (array): The image where the number of relationships will be obtained
			matrix (array): 

		Returns:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
		"""
		# Reads the image from the fila
		image = cv2.imread(image_file_location, 0)

		pixels = read_text_files(pixels_file_location)

		pixels_array = string_array_to_int_array(pixels)

		hotizontal_relationships = self.hotizontal_relationship(image, pixels_array)

		matrix_up = hotizontal_relationships[0]
		matrix_down = hotizontal_relationships[1]
		glcm_matrix = hotizontal_relationships[2]

		number_of_relationships = float((matrix_left.shape[0]-1)*matrix_left.shape[1]) + float((matrix_right.shape[0]-1)*matrix_right.shape[1])
		print(number_of_relationships)
		glcm_percentage_matrix = glcm_horizontal_matrix * (1.0/number_of_relationships)
		glcm_percentage_matrix = numpy.around(glcm_percentage_matrix, decimals=3)

		return glcm_percentage_matrix
