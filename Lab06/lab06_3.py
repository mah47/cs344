'''
Marcos Hernandez (mah47)
March 14, 2020
CS344
'''


import numpy as np
from keras.datasets import mnist
from tensorflow.python.keras.datasets import boston_housing
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images),
                train_images.ndim,
                train_images.shape,
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \
            \n\tvalues: {}\n'.format(
                len(test_labels),
                train_labels.ndim,
                test_labels.shape,
                test_labels.dtype,
                test_labels
        )
    )
print_structures()

'''
Lab6_3 Results
1. 
    There are 404 training images and 102 testing images
2. 
    2 axes/dimensions, shape = 404, 13, data type = float64
    1 axe/dimension, shape = 102, data type = float64 
'''