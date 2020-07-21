import numpy as np 

X = np.random.normal(0, 1, (20, 20))
y = np.random.randint(2, size=(20,1), dtype='int32')

theta = np.dot(np.dot(np.linalg.pinv(np.dot(X.T, X)), X.T), y)
print(theta)