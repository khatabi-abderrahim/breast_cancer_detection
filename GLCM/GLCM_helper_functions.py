import cv2
import numpy

def string_array_to_int_array(string_array):
	"""
	Takes an array  made of one string with every unique pixel of an image from the
	dataset and turns it into an integer array.

	Arguments:
		string_array (array): An integer element array.

	Returns:
		string_array (array): An integer element array.
	"""	
	integer_array = []
	for list_element in range(0, len(string_array)):
		string_array[list_element] = string_array[list_element].replace("\n","")
		string_array[list_element] = string_array[list_element].replace("[","")
		string_array[list_element] = string_array[list_element].replace("]"," ")
		string_array[list_element] = string_array[list_element].replace("  ",",")
		string_array[list_element] = string_array[list_element].replace(" ",",")
		string_array[list_element] = string_array[list_element].split(',')

	for list_element in range(0, len(string_array)):
		string_array[list_element] = list(filter(None, string_array[list_element]))
		string_array[list_element] = [float(element) for element in string_array[list_element]]
		integer_array = numpy.append(integer_array,string_array[list_element])

	return integer_array