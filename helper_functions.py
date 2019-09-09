def read_text_files(link_to_file):
	"""
	Reads the given text file to extract the information

	Arguments:
		link_to_file (String): The string containing the link to the file

	Returns:
		read_file (String): The infomration gotten from the image
	"""
	file = open(link_to_file,"r")
	read_file = file.readlines()
	file.close()

	return read_file