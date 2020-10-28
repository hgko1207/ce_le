import numpy as np
from scipy.stats import norm
from math import *
from scipy import special

def erfcc(x):
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
        t*(.09678418+t*(-.18628806+t*(.27886807+
        t*(-1.13520398+t*(1.48851587+t*(-.82215223+
        t*.17087277)))))))))
    if (x >= 0.):
        return r
    else:
        return 2. - r

# 정규분포의 누적분포함수
def normcdf(x, mu, sigma):
    t = x - mu;
    y = 0.5 * erfcc (-t / (sigma * np.sqrt(2.0)));
    if y > 1.0:
        y = 1.0;
    return y

# 공분산
covariance = 9
# 표준편차
stdev = np.sqrt(covariance)
# 확률
p = 90/100
# 오차 역함수
erfinv = special.erfinv(p)

LE_90 = stdev * np.sqrt(2) * erfinv
print("확률계수 : ", round(np.sqrt(2) * erfinv, 4))
print("LE_90 = ", round(LE_90, 2), "meters")



