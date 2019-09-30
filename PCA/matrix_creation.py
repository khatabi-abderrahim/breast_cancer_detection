import numpy
from helper_functions import read_text_files
from GLCM.GLCM_helper_functions import string_array_to_int_array

class  MatrixCreation():
	"""
	Create the PCA matrix with the GLCM variables of every image in the dataset.
	"""
	def independent_variable_labels(self):
		"""
		Creates a dictionary for the independent variable lables, that stores the column
		and the GLCM texture that it stores.

		Returns:
			matrix_labels (dictionary): The key holds the number of column, while the value
										hold the texture to be measured and the direction of
										the relationship in the GLCM.
										'[texture]_[GLCM direction]'
		"""
		texture_matrix_labels = {
			0: 'image reference'
			1: 'contrast right',
			2: 'contrast left',
			3: 'contrast up',
			4: 'contrast down',
			5: 'energy right',
			6: 'energy left',
			7: 'energy up',
			8: 'energy down',
			9: 'dissimilarity right',
			10: 'dissimilarity left',
			11: 'dissimilarity up',
			12: 'dissimilarity down',
			13: 'homogeneity right',
			14: 'homogeneity left',
			15: 'homogeneity up',
			16: 'homogeneity down',
			17: 'correlation right',
			18: 'correlation left',
			19: 'correlation up',
			20: 'correlation down',
			21: 'asm right',
			22: 'asm left',
			23: 'asm up',
			24: 'asm down'
		}
		return texture_matrix_labels

	def extract_data(self, file_location):
		"""
		Extracts the texture data from the image text file as a two dimensional
		numpy array or the dependent variables.

		Arguments:
			file_location (integer): A string containing the directory of the file where
									 the data will be extracted

		Returns:
			file_data (array): A two dimensional array with the texture measurements of the
							   given image_number 
		"""
		if file_location.split(".")[1] == 'txt':
			file_data = read_text_files(file_location)
			file_data = string_array_to_int_array(file_data)
			file_data = numpy.array(file_data)
			file_data = numpy.reshape(a=file_data,newshape=(1,25))
		
		elif file_location.split(".")[1] == 'csv':
			file_data = []
			with open(file='all-mias/images_clasifications.csv') as csvDataFile:
				csvReader = csv.reader(csvDataFile)
				for row in csvReader:
					file_data.append(row)
			file_data = numpy.array(file_data)

		return file_data

	def create_texture_matrix(self):
		"""
		Constructs a matrix with every texture data from the image dataset to later
		calculate the Principal Components Analyisis

		Returns:
			texture_matrix(array): A two dimensional array with the texture measurements of the
							       entire dataset
		"""
		texture_matrix = self.extract_data(file_location="GLCM/matrix/textures_mdb1.txt")

		for image_number in range(2,323):
			texture_matrix = numpy.append(texture_matrix, self.extract_data(file_location="GLCM/matrix/textures_mdb{}.txt".format(image_number)), axis=0)

		return texture_matrix
	
	def create_full_matrix(self):
		"""
		Creates a matrix with both the independent variables (GLCM texture features) and
		dependent variables (image classifiers: character of background tissue (fatty,
		fatty-glandular, dense-glandular), class of abnormality present (calcification,
		well-defined/circumscribed masses, spiculated masses, other, ill-defined masses,
		architectural distortion,asymmetry or if it's normal) and severity of
		abnormality (beningn, malignant).)
		"""
		texture_matrix = self.create_texture_matrix()

		image_clasifications_matrix = self.extract_data("all-mias/images_clasifications.csv")

		data_matrix = numpy.zeros(shape=(image_clasifications_matrix.shape[0],texture_matrix.shape[1]+image_clasifications_matrix.shape[1]-2))

		for row in range(0,image_clasifications_matrix.shape[0]-1):
			for glcm_row in range(0,texture_matrix.shape[0]-1):
				if int(texture_matrix[glcm_row,0]) == int(image_clasifications_matrix[row,0].split('mdb')[1]):
					data_matrix[row] = numpy.append(texture_matrix[glcm_row,range(1,texture_matrix.shape[1])],image_clasifications_matrix[row,range(1,image_clasifications_matrix.shape[1])].astype(int) )

		return data_matrix