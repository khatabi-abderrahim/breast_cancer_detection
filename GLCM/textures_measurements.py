from skimage import feature
import numpy
from GLCM.pixel_matrix import CoOcurrencyMatrix
from helper_functions import write_text_files
from PCA.pca_interpretation import PCAComponentsInterpretation

class TextureMeasurements():
	"""
	They are Energy, Entropy, Contrast, Correlation, and  Homogeneity. Energy
	returns the sum  of  squared elements in the GLCM and the range will be in
	[0, 1]. Entropy measures the randomness  of  intensity  distribution.
	Correlation measure of  image  linearity, and Homogeneity Returns a value that
	measures the closeness of the distribution of elements in the GLCM to the GLCM
	diagonal and range will be in [0 1].
	"""
	def save_texture_measurements(self, image_number, image_file_location):
		"""
		From the GLCM matrix, create an array with the calculations of the texture
		measurements (contrast, energy, dissimilarity, homogeneity, correlation, asm)
		and save them in a text file.
		Contrast: Measures the  amount  of local  variation  in  the  image.

		Args:
			image_number (number): A number that identifies the image to be analyzed
			image_file_location (string): The location where the image is stored

		Returns:
			(string): The location of where the contrast information 
					  of the matrix will be saved
		"""
		glcm_percentage_matrix = CoOcurrencyMatrix().relationship_probabilities(image_file_location)

		contrast = self.extract_texture_measurement(glcm_percentage_matrix, texture='contrast')
		energy = self.extract_texture_measurement(glcm_percentage_matrix, texture='energy')
		dissimilarity = self.extract_texture_measurement(glcm_percentage_matrix, texture='dissimilarity')
		homogeneity = self.extract_texture_measurement(glcm_percentage_matrix, texture='homogeneity')
		correlation = self.extract_texture_measurement(glcm_percentage_matrix, texture='correlation')
		asm = self.extract_texture_measurement(glcm_percentage_matrix, texture='ASM')

		textures = numpy.concatenate((contrast,energy,dissimilarity,homogeneity,correlation,asm),axis=0)
		textures = numpy.insert(arr=textures,obj=0,values=image_number)

		write_text_files(link_to_file="GLCM/matrix/textures_mdb{}.txt".format(image_number), result_data=textures)

		return "GLCM/matrix/textures_mdb{}.txt".format(image_number)

	def extract_texture_measurement(self, glcm_percentage_matrix, texture):
		"""
		Extract the texture measurements of the image from the four glcm percentage
		matrix vertical and horizontal direction.
		
		Args:
			glcm_percentage_matrix (array): The percentage of the relationship between
											two pixels in the image
			texture (string): The texture property to be calculated from the GLCM matrix

		Returns:
			extracted_texture (array): The texture measurements of the GLCM with
							  		   vertical and horizontal direction.
		"""
		extracted_texture = feature.greycoprops(glcm_percentage_matrix, prop=texture).flatten()

		return extracted_texture	