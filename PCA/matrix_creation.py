import numpy
from helper_functions import read_text_files
from GLCM.GLCM_helper_functions import string_array_to_int_array

class  MatrixCreation():
	"""
	Create the PCA matrix with the GLCM variables of every image in the dataset.
	"""
	def matrix_labels(self):
		"""
		Creates a dictionary that stores the column and the txture that it stores.

		Returns:
			matrix_labels (dictionary): The key holds the number of column, while the value
										hold the texture to be measured and the direction of
										the relationship in the GLCM.
										'[texture]_[GLCM direction]'
		"""
		matrix_labels = {
			0: 'contrast_right',
			1: 'contrast_left',
			2: 'contrast_up',
			3: 'contrast_down',
			4: 'energy_right',
			5: 'energy_left',
			6: 'energy_up',
			7: 'energy_down',
			8: 'dissimilarity_right',
			9: 'dissimilarity_left',
			10: 'dissimilarity_up',
			11: 'dissimilarity_down',
			12: 'homogeneity_right',
			13: 'homogeneity_left',
			14: 'homogeneity_up',
			15: 'homogeneity_down',
			16: 'correlation_right',
			17: 'correlation_left',
			18: 'correlation_up',
			19: 'correlation_down',
			20: 'asm_right',
			21: 'asm_left',
			22: 'asm_up',
			23: 'asm_down'
		}
		return matrix_labels

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
		"""
		Constructs a matrix with every texture data from the image dataset to later
		calculate the Principal Components Analyisis

		Returns:
			texture_matrix(array): A two dimensional array with the texture measurements of the
							       entire dataset
		"""
		texture_matrix = self.extract_data(image_number=1)

		for image in range(2,322):
			texture_matrix = numpy.append(texture_matrix, self.extract_data(image_number=image), axis=0)

		return texture_matrix