import numpy as np

test1 = np.array([1,2,3,4,5])
print('test1 : ',test1)

test2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print('test2 : ',test2)

test3 = np.array([[[1,2,3,4,5],[1,2,3,4,5]], [[1,2,3,4,5],[1,2,3,4,5]]])
print('test3 : ',test3)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 2, 3)

print(newarr)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

