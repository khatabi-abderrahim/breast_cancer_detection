from celery import Celery
import numpy
from GLCM.pixel_matrix import co_ocurrency_matrix_vertical, co_ocurrency_matrix_horizontal
from helper_functions import write_text_files

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task()
def get_vertical_glcm_matrix(image_number, image_file_location, pixels_file_location):
	"""
	This function is made to delegate the GLCM vertical relationship calculations
	in an asynchronous way.

	Arguments:
		image_file_location
	"""	
	
	result = co_ocurrency_matrix_vertical().vertical_relationship_probabilities(image_number, image_file_location, pixels_file_location)

	return result

@app.task()
def get_horizontal_glcm_matrix(image_number, image_file_location, pixels_file_location):
	"""
	This function is made to delegate the GLCM horizontal relationship calculations
	in an asynchronous way.

	Arguments:
		image_file_location
	"""	
	
	result = co_ocurrency_matrix_horizontal().horizontal_relationship_probabilities(image_number, image_file_location, pixels_file_location)

	return result