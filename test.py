import numpy as np

a = [1,2].sort()
b = [2,1].sort()


a1 = np.array(a)
a2 = np.array(b)

print(a1 == a2)