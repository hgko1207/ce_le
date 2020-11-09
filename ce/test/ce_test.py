import math
from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.linalg import sqrtm
import numpy as np
import random

avgs = np.array([10, 5])
avgs = np.array([1, -3])
covariances = np.array([[10 ** 2, 0.75 * 10 * 12], [0.75 * 10 * 12, 12 ** 2]])
covariances = np.array([[4, 2], [2, 3]])
covariances = sqrtm(covariances) # 행렬제곱근
print(avgs)
print(covariances)

ni = np.random.randn(1000000, 2)

results = []
xValues = []
yValues = []

for x in ni:
    num = np.array([x[0], x[1]])
    result =  avgs + np.matmul(covariances, num)
    xValues.append(result[0])
    yValues.append(result[1])
    results.append(math.sqrt(result[0] ** 2 + result[1] ** 2))

results.sort()
print("first : ", results[0])
print("center : ", results[500000])
print("CE_95 : ", (results[950001] + results[950001]) / 2)
print("CE_90 : ", (results[900000] + results[900001]) / 2)

plt.scatter(xValues, yValues)
plt.title('Various Normal pdfs')
plt.show()