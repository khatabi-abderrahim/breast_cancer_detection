import cv2
import numpy

def reduce_images(image):
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
	for array_element in range(0,len(string_array)):
		string_array[array_element] = string_array[array_element].replace("\n","")
		string_array[array_element] = string_array[array_element].replace("[","")
		string_array[array_element] = string_array[array_element].replace("]"," ")
		string_array[array_element] = string_array[array_element].replace("  ",",")
		string_array[array_element] = string_array[array_element].replace(" ",",")
		string_array[array_element] = string_array[array_element].split(',')

		for index, element in enumerate(string_array[array_element]):
			if len(element) == 0:
				del string_array[array_element][index]

		string_array[array_element] = [float(element) for element in string_array[array_element]]

	return string_array