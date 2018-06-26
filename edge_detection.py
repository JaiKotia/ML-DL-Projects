import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy import misc
from PIL import Image

im=Image.open('<insert image here>')

img_grey=im.convert("L")

print("\n Original type: %r \n\n" % img_grey)

arr = np.asarray(img_grey) 
print("After conversion to numerical representation: \n\n %r" % arr) 

imgplot = plt.imshow(arr)

kernel = np.array([
                        [ 0, 1, 0],
                        [ 1,-4, 1],
                        [ 0, 1, 0],
                                     ]) 

grad = signal.convolve2d(arr, kernel, mode='same', boundary='symm')

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(np.absolute(grad), cmap='gray')

type(grad)

grad_biases = np.absolute(grad) + 100

grad_biases[grad_biases > 255] = 255

print('GRADIENT MAGNITUDE - Feature map')

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(np.absolute(grad_biases), cmap='gray')








