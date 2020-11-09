import numpy as np

# 1) 공분산 값
covariances = np.array([[4, 2], [2, 3]])

# 2) 고유값 계산
w, v = np.linalg.eig(covariances)

# 3) 최대, 최소 고유값에 제곱근
sigmamax = np.sqrt(w[0])
sigmamin = np.sqrt(w[1])

# 4) 확률계수를 구한다.
r = sigmamin / sigmamax
r = round(r, 3)
p = 0.5

# 4-1) Linear Interpolation
first = 1.7371
second = 1.7621

x1 = r - p
x2 = 0.05 - x1
R = (x2 / 0.05) * first + (x1 / 0.05) * second

# CE 90 계산
CE_90 = round(R * sigmamax, 2)
print("CE_90 = ", CE_90, "meters")


