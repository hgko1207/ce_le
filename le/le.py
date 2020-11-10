import numpy as np
from scipy.stats import norm
from math import *
from scipy import special
import csv

def erfcc(x):
    """Complementary error function."""
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * exp(-z * z-1.26551223 + t * (1.00002368 + t * (.37409196 +
        t * (.09678418 + t * (-.18628806 + t * (.27886807+
        t * (-1.13520398 + t * (1.48851587 + t * (-.82215223 +
        t * .17087277)))))))))
    if (x >= 0.):
        return r
    else:
        return 2. - r

def normcdf(x, mu, sigma):
    t = x - mu;
    y = 0.5 * erfcc (-t / (sigma * np.sqrt(2.0)));
    if y > 1.0:
        y = 1.0;
    return y

def le_90_avg_0(zErrors):
     # 분산
    var = np.var(zErrors)

    # 표준편차
    stdev = np.sqrt(var)

    # 확률
    p = 90/100

    # 오차 역함수
    erfinv = special.erfinv(p)
    print("확률계수 : ", round(np.sqrt(2) * erfinv, 4))

    return stdev * np.sqrt(2) * erfinv

def le_90(zErrors):
    # 분산
    var = np.var(zErrors)

    # 표준편차
    stdev = np.sqrt(var)

    print("평균 : " , avg)
    print("분산 : " , var)
    print("표준편차 : " , stdev)

    # 1. 잔차를 정렬 후 90%에 해당하는 변수를 확률변수로 사용하여 계산
    zErrors.sort()
    num = int(len(zErrors) * 0.9)

    z = zErrors[num]
    p = normcdf(z, avg, stdev)

    # 2. 잔차의 최소, 최대 값에 대한 CDF를 계산한다.(잔차의 최소와 최대 사이일 확률을 구하는 것)
    # min_n = np.min(zErrors)
    # max_n = np.max(zErrors)

    # min_p = normcdf(min_n, avg, stdev)
    # max_p = normcdf(max_n, avg, stdev)
    # p = max_p - min_p

    erfinv = special.erfinv(p)
    print("확률계수 : ", round(np.sqrt(2) * erfinv, 4))

    return stdev * np.sqrt(2) * erfinv


if __name__ == "__main__":
    file = open('../data/letest.csv', 'r', encoding='utf-8')
    rdf = csv.reader(file)

    zErrors = []

    for line in rdf:
        zErrors.append(float(line[0]))
    file.close()

    # 평균
    avg = np.mean(zErrors)

    if (avg == 0):
        print("LE_90 = ", le_90_avg_0(zErrors), "meters")
    else:
        print("LE_90 : ", le_90(zErrors), "meters")
