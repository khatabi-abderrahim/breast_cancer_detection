
# Breast Cancer Detection
Extract image textures using Grey Level Co-Ocurrency Matrix (GLCM) calculations

## Packages needed
OpenCV
OpenCV (Open Source Computer Vision Library: http://opencv.org) is an open-source BSD-licensed library that includes several hundreds of computer vision algorithms.
```bash
pip install opencv-python
```

Numpy
NumPy is the fundamental package needed for scientific computing with Python
```bash
pip install numpy
```

Celery
A distributed Task Queue.
```bash
brew install celery
```
Start celery
```bash
 celery -A tasks worker --loglevel=info
```

Rabbitmq
An open-source message-broker software.
```bash
brew install rabbitmq
```
Start the broker
```bash
brew services start rabbitmq
```

Celery flower
Flower is a web based tool for monitoring and administrating Celery clusters.
```bash
pip install flower
```
Start flower
```bash
flower --port=5555
```
