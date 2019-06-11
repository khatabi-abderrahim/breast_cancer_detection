import cv2
import numpy as np
from GLCM.pixel_matrix import number_of_pixels, create_matrix, pixel_relationship

image = cv2.imread('all-mias/mdb001.pgm',0)
image_shape = image.shape
image_rows = image_shape[0]
image_columns = image_shape[1]

pixels = number_of_pixels(image, image_rows, image_columns)
print(pixels)

matrix = create_matrix(pixels)
print(matrix)

print(matrix.shape)

pixel_rel = pixel_relationship(image, image_rows, image_columns, pixels[0], pixels[0])
print("number of relationships (0,0) : {}".format(pixel_rel))