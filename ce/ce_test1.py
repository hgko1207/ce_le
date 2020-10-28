import math
from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.linalg import sqrtm
import numpy as np
import random

# y = []
# for x in range(0, 100):
#     y.append(stats.norm(0, 1).pdf(x))
#     # plt.scatter(x, y)
# print(y)

# x = np.linspace(stats.norm.ppf(.01), stats.norm.ppf(.99), 100)
# print(x)

avgs = np.array([10, 5])
avgs = np.array([1, -3])
covariances = np.array([[10 ** 2, 0.75 * 10 * 12], [0.75 * 10 * 12, 12 ** 2]])
covariances = np.array([[4, 2], [2, 3]])
covariances = sqrtm(covariances) # 행렬제곱근
print(avgs)
print(covariances)

# x = np.random.normal(size=1000000)

# x = -0.146382
# num = np.array([x, x])
# print("matmul : ", np.matmul(covariances, num))

# s =  avgs + np.matmul(covariances, num)
# print("s : ", s)
# result = math.sqrt(s[0] ** 2 + s[1] ** 2)
# print(result)

results = []
xValues = []
yValues = []
for i in np.arange(1, 1000000):
  num = np.array([random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)])
  result =  avgs + np.matmul(covariances, num)
  xValues.append(result[0])
  yValues.append(result[1])
  results.append(math.sqrt(result[0] ** 2 + result[1] ** 2))

results.sort()
print("first : ", results[0])
print("center : ", results[500000])
print("CE_95 : ", results[950001])
print("CE_90 : ", (results[900000] + results[900001]) / 2)

plt.scatter(xValues, yValues)
plt.title('Various Normal pdfs')
plt.show()
