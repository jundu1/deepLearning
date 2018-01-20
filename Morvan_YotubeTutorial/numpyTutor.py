import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]])

A = np.arange(2,14).reshape((3,4))
print(A)
# print(np.argmin(A))
# print(np.argmax(A))
# print(np.average(A))
# print(np.mean(A))
print(np.nonzero(A))
print(A[np.nonzero(A)])