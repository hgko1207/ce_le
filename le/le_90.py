import numpy as np
from scipy.stats import norm
from math import *
from scipy import special

def erfcc(x):
    """Complementary error function."""
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

# 평균 값
avg = -2
# 공분산
covariance = 9
# 표준편차
stdev = np.sqrt(covariance)

x = 3.044
p = normcdf(x, avg, stdev)
erfinv = special.erfinv(p)

LE_90 = stdev * np.sqrt(2) * erfinv

print("확률계수 : ", round(np.sqrt(2) * erfinv, 4))
print("LE_90 : ", LE_90, "meters")