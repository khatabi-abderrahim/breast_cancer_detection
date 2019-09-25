import numpy
from PCA.pca_calculation import PCACalculation
from PCA.matrix_creation import MatrixCreation

"""
Script to calculate the principal components from the texture measurements
of every image from the data set
"""

glcm_texture_measurements = MatrixCreation().create_matrix()
pca = PCACalculation().calculate_principal_components(glcm_texture_measurements)
print(pca)