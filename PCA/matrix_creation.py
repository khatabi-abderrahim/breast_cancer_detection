import numpy
from helper_functions import read_text_files
from GLCM.GLCM_helper_functions import string_array_to_int_array

class  MatrixCreation():
	"""
	Create the PCA matrix with the GLCM variables of every image in the dataset.
	"""
	def extract_data(self, image_number):
		"""
		Extracts the texture data from the image text file as a two dimensional
		numpy array

		Arguments:
			image_number (integer): The number of the image ti extract the data

		Returns:
			file_data (array): A two dimensional array with the texture measurements of the
							   given image_number 
		"""
		file_data = read_text_files("GLCM/matrix/textures_mdb{}.txt".format(image_number))
		file_data = string_array_to_int_array(file_data)
		file_data = numpy.array(file_data)
		file_data = numpy.reshape(a=file_data,newshape=(1,24))

		return file_data  

	def create_matrix(self):
		pass	