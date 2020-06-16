# import libraries
import numpy as np

# create a 1D array of 20 random floats
original = np.random.uniform(low=1, high=20, size=20)
print("Original: \n", original)

# reshape the 1D array to a 4x5
new = original.reshape((4, 5))
print("Reshaped: \n", new)

# find the max value of each row and replace by 0, but keep all other dimensions
x = np.where(new == np.max(new, axis=1, keepdims=True), 0*new, new)
print("Replaced: \n", x)
