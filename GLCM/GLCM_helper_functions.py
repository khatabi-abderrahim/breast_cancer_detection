import cv2
import numpy

def redude_images(image):
	"""
	Takes an image and reduces its black square spots

	Arguments:
		image (array): The image as numpy array

	Returns:
		image (array): A diminished image as numpy array
	"""
	zero_pixels = []

	for column in range(0,image.shape[1]):
		if numpy.sum(image[:,column]) <= 11 :
			zero_pixels.append(column)

	image = numpy.delete(image, zero_pixels, 1)

	return image

def string_array_to_int_array(string_array):
	"""
	Takes an array  made of one string with every unique pixel of an image from the
	dataset and turns it into an integer array.

	Arguments:
		string_array (array): An integer element array.

	Returns:
		string_array (array): An integer element array.
	"""
	
	string_array[0] = string_array[0].replace("[","")
	string_array[0] = string_array[0].replace("]","")
	string_array = string_array[0].split(",")

	for string_element in string_array:
		string_element = string_element.replace(" ","")

	number_array = [int(string_element, base=16) for string_element in string_array] 

	return number_array