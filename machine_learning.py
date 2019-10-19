import numpy
from ML.knn_algorithm import KnnAlgorithm
from ML.svm_algorithm import SvmAlgorithm
from ML.logistic_regresion_algorithm import LogisticRegresionAlgorithm
from ML.algorithm_metrics import ConfusionMatrix
from ML.svm_algorithm import SvmAlgorithm
from ML.prepare_data import PrepareData

"""
Compare the performance of three different classifiers: Nearest Neighbor, Suport
Vector Machine and Logistic Regression.
"""
print("Nearest Neighbor")
knn_classifier = KnnAlgorithm().make_predictions()
knn_metrics = ConfusionMatrix(predicted_results=knn_classifier).get_metrics()
print(knn_metrics)

print("Suport Vector Machine")
svm_classifier = SvmAlgorithm().join_predictions()
svm_metrics = ConfusionMatrix(predicted_results=svm_classifier).get_metrics()
print(svm_metrics)

print("Logistic Regression")
logistic_regresion_classifier = LogisticRegresionAlgorithm().join_predictions()
logistic_regresion_metrics = ConfusionMatrix(predicted_results=logistic_regresion_classifier).get_metrics()
print(logistic_regresion_metrics)