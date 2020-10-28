import csv
import math
import numpy as np
from scipy.linalg import sqrtm
from matplotlib import pyplot as plt
import scipy.stats

f = open('data/cetest1.csv', 'r', encoding='utf-8')
rdf = csv.reader(f)

xErrors = []
yErrors = []

for line in rdf:
  xErrors.append(float(line[0]))
  yErrors.append(float(line[1]))
f.close()

# 평균 값
avgs = np.array([np.mean(xErrors), np.mean(yErrors)])

# 공분산 행렬
covariances = np.cov(xErrors, yErrors)

print(covariances)

# 1) 공분산 행렬 제곱근
covariances = sqrtm(covariances)

print("avgs = ", avgs)
print("covariances = ", covariances)

plt.figure(figsize=(8,6))
plt.scatter(x=xErrors, y=yErrors, s=2, c='blue', alpha=1, label='errors')
plt.title('Convariance Square Root Magnitude Ordering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()