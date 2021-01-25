import numpy as np

a = np.array([[1, 0, 2, 1], [0, 5, 1, 1]])
b = np.array([[1, 0], [0, 1]])

if __name__ == "__main__":
    print(a.shape)
    print(b.shape)
    print(np.dot(a.T, b).dot(a))
