from celery import Celery
import numpy
from GLCM.textures_measurements import TextureMeasurements
from helper_functions import write_text_files

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task()
def get_texture_glcm_measurements(image_number, image_file_location):
	"""
	This function is made to delegate the calculationd of the texture features
	of the GLCM in an asynchronous way.

	Arguments:
		image_file_location (string): The location of the image
		image_number (number): A number that identifies the image to be analyzed

	Returns:
		result (string): Returns the 
	"""	
	result = TextureMeasurements().contrast_measurements(image_number, image_file_location)

	return result