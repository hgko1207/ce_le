import csv
import math
import numpy as np
from scipy.linalg import sqrtm
from matplotlib import pyplot as plt

f = open('data/cetest2.csv', 'r', encoding='utf-8')
rdf = csv.reader(f)

xErrors = []
yErrors = []

for line in rdf:
  xErrors.append(float(line[0]))
  yErrors.append(float(line[1]))
f.close()

# 평균 값
avgs = np.array([np.mean(xErrors), np.mean(yErrors)])
# avgs = np.array([10, 5])
# avgs = np.array([1, -3])

# 공분산 행렬
covariances = np.cov([xErrors, yErrors])
# covariances = np.array([[10 ** 2, 0.75 * 10 * 12], [0.75 * 10 * 12, 12 ** 2]])
# covariances = np.array([[4, 2], [2, 3]])

# 1) 공분산 행렬 제곱근
covariances = sqrtm(covariances)

print("avgs = ", avgs)
print("covariances = ", covariances)

# 2) 정규 랜덤 변수 생성
n = 10000
ni = np.random.randn(n, 2)

results = []
xValues = []
yValues = []

# 3) Si 계산
for x in ni:
    num = np.array([x[0], x[1]])
    s =  avgs + np.matmul(covariances, num)
    xValues.append(s[0])
    yValues.append(s[1])
    results.append(math.sqrt(s[0] ** 2 + s[1] ** 2))

# 4) 정렬
results.sort()

# 5) 90%의 가장 큰 크기 및 다음 크기의 값 지정
n50 = int(n * 0.5)
n90 = int(n * 0.9)
n95 = int(n * 0.95)
print(n90, results[n90], results[n90 + 1])

tests = results[n90:]
print(np.min(results))

CE50 = (results[n50] + results[n50 + 1]) / 2
CE90 = (results[n90] + results[n90 + 1]) / 2
CE95 = (results[n95] + results[n95 + 1]) / 2
print("CE_50 = ", CE50)
print("CE_90 = ", CE90)
print("CE_95 = ", CE95)

figure, axes = plt.subplots()
axes.set_aspect(1)

ce90_circle = plt.Circle((0, 0), radius=CE90, fill=False, color='green', alpha=1)
plt.gca().add_patch(ce90_circle)

plt.scatter(x=xValues, y=yValues, s=0.5, c='blue', alpha=1, label='errors')
# plt.scatter(x=results, y=results, s=0.5, c='red', alpha=0.5, label='errors')
plt.title('Convariance Square Root Magnitude Ordering')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.show()