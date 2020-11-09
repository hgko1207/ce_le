import csv
import math
import numpy as np
from scipy.linalg import sqrtm
from matplotlib import pyplot as plt
import ceconstant

# 평균이 0일 때 CE 계산
def ce_90_avg_0(xErrors, yErrors):
    # 1) 공분산 값
    covariances = np.cov([xErrors, yErrors])

    # 2) 고유값 계산
    w, v = np.linalg.eig(covariances)

    # 3) 최대, 최소 고유값에 제곱근
    sigmamax = np.sqrt(w[0])
    sigmamin = np.sqrt(w[1])

    # 4) 확률계수를 구한다.
    r = sigmamin / sigmamax
    r = round(r, 3)

    # 4-1) Linear Interpolation
    R = ceconstant.linearInterpolation(r)

    print("sigmamax : ", sigmamax)
    print("R : ", R)

    # CE 90 계산
    return R * sigmamax

# 평균이 0이 아닐 때 CE 계산
def ce_90(xErrors, yErrors):
    # 공분산 행렬
    covariances = np.cov([xErrors, yErrors])

    # 1) 공분산 행렬 제곱근
    covariances = sqrtm(covariances)

    # 2) 정규 랜덤 변수 생성
    n = 1000000
    ni = np.random.randn(n, 2)

    results = []

    # 3) Si 계산
    for x in ni:
        num = np.array([x[0], x[1]])
        s =  avgs + np.matmul(covariances, num)
        results.append(math.sqrt(s[0] ** 2 + s[1] ** 2))

    # 5) 90%의 가장 큰 크기 및 다음 크기의 값 지정
    n90 = int(n * 0.9)

    return (results[n90] + results[n90 + 1]) / 2
    

if __name__ == "__main__":
    file = open('../data/cetest.csv', 'r', encoding='utf-8')
    rdf = csv.reader(file)

    xErrors = []
    yErrors = []

    for line in rdf:
        xErrors.append(float(line[0]))
        yErrors.append(float(line[1]))
    file.close()

    # 평균 값 계산
    avgs = np.array([np.mean(xErrors), np.mean(yErrors)])

    if (avgs[0] == 0 and avgs[1] == 0):
        print("CE_90 = ", ce_90_avg_0(xErrors, yErrors), "meters")
    else:
        print("CE_90 = ", ce_90(xErrors, yErrors), "meters")