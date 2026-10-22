import numpy as np

# 1. Create an array containing 1, 2, 3, 4, 5
arr1 = np.array([1, 2, 3, 4, 5])

# 2. Create an array of five zeros
arr2 = np.zeros(5)

# 3. Create an array of even numbers from 2 to 10
arr3 = np.arange(2, 11, 2)

# 4. Create five evenly spaced numbers from 0 to 1
arr4 = np.linspace(0, 1, 5)

# Bonus: Create a 2D array with two rows and three columns
arr5 = np.array([[1, 2, 3], [4, 5, 6]])

# Expected Output:
arr1  # [1 2 3 4 5]
arr2  # [0. 0. 0. 0. 0.]
arr3  # [ 2  4  6  8 10]
arr4  # [0.   0.25 0.5  0.75 1.  ]
arr5  # [[1 2 3]
#  [4 5 6]]
