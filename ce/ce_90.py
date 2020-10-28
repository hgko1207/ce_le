import math
import numpy as np
from scipy.linalg import sqrtm

# 평균 값
avgs = np.array([1, -3])
# 공분산 행렬
covariances = np.array([[4, 2], [2, 3]])

# 1) 공분산 행렬 제곱근
covariances = sqrtm(covariances)

# 2) 정규 랜덤 변수 생성
n = 100000
ni = np.random.randn(n, 2)

results = []

# 3) Si 계산
for x in ni:
    num = np.array([x[0], x[1]])
    s =  avgs + np.matmul(covariances, num)
    results.append(math.sqrt(s[0] ** 2 + s[1] ** 2))

# 4) 정렬
results.sort()

# 5) 90%의 가장 큰 크기 및 다음 크기의 값 지정
n90 = int(n * 0.9)
RE_90 = results[n90]
RE_90_1 = results[n90 + 1]

# 6) CE 90 계산
CE90 = (RE_90 + RE_90_1) / 2
print("CE_90 = ", round(CE90, 2), "meters")


