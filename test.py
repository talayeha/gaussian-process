import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [3, 5]])
print(np.log(np.diagonal(a) / np.diagonal(b)))
