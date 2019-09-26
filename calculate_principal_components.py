import numpy
from PCA.pca_calculation import PCACalculation
from PCA.matrix_creation import MatrixCreation

"""
Script to calculate the principal components from the texture measurements
of every image from the data set
"""

glcm_texture_measurements = MatrixCreation().create_matrix()

example_data = numpy.array([
[102, 42,	85.4,	1.8,	5.1,  63,	30],
[117, 51,	94.2,	2.1,	3.8,  70,	14],
[116, 49,	95.3,	1.98,	8.2,  72,	14],
[117, 50,	94.7,	2.01,	5.8,  73,	97],
[112, 51,	89.4,	1.86,	7,	  72,	95],
[120, 38,	99.5,	2.25,	9.3,  71,	10],
[121, 29,	99.8,	2.1,	2.5,  69,	42],
[110, 47,	90.9,	1.9,	6.2,  66,	8],
[111, 49,	89.2,	1.7,	7.1,  69,	60],
[117, 48,	92.7,	2.09,	5.6,  64,	35],
[112, 47,	94.4,	2.07,	5.3,  74,	90],
[115, 49,	94.1,	1.92,	5.6,  71,	21],
[114, 50,	91.6,	2.05,	10.2, 68,	47],
[110, 47,	87.1,	1.92,	5.6,  67,	80],
[125, 52,	101.3,	2.19,	10,	  76,	98],
[112, 46,	94.5,	1.98,	7.4,  69,	98],
[106, 46,	87,	    1.87,	3.6,  62,	13],
[109, 46,	94.5,	1.9,    4.3,  70,	15],
[112, 48,	90.5,	1.88,	9,	  71,	99],
[120, 56,	95.7,	2.09,	7,	  75,	94],
])

pca_example = PCACalculation().calculate_principal_components(example_data)
pca_all_mias = PCACalculation().calculate_principal_components(glcm_texture_measurements)