# Q is list is an array ?
# no array is collection of elements of same datatype.


import numpy as np
import pandas as pd
arr = np.array([1,2,3,4,5])
print(type(arr))
df = pd.DataFrame(arr)
l1 = [10, 20, 30]

print(type(l1))
print(df)
