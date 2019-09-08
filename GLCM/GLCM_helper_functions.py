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
		string_element = int(string_element)

	return string_array