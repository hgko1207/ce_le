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

def normpdf(x, mu, sigma):
    u = (x - mu) / abs(sigma)
    y = (1 / (sqrt(2 * pi) * abs(sigma))) * exp(-u * u/2)
    return y

def normdist(x, mu, sigma, f):
    if f:
        y = normcdf(x,mu,sigma)
    else:
        y = normpdf(x,mu,sigma)
    return y

f = open('data/letest.csv', 'r', encoding='utf-8')
rdf = csv.reader(f)

zErrors = []

for line in rdf:
  zErrors.append(float(line[0]))
f.close()

# 평균
avg = np.mean(zErrors)

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

LE_90 = stdev * np.sqrt(2) * erfinv

print("확률계수 : ", round(np.sqrt(2) * erfinv, 4))
print("LE_90 : ", LE_90, "meters")