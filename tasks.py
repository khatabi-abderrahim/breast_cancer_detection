from celery import Celery
import numpy
from GLCM.pixel_matrix import co_ocurrency_matrix_vertical

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task()
def get_vertical_glcm_matrix(image_number, image_file_location, pixels_file_location):
	"""
	This function is made to delegate the GLCM vertical relationship calculations
	in an asynchronous way.

	Arguments:
		image_file_location
	"""
	
	co_ocurrency_matrix_vertical().vertical_relationship_probabilities(image_number, image_file_location, pixels_file_location)

	return None