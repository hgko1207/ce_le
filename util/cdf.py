import math
from matplotlib import pyplot as plt

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-60,60)]
# plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
# plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
# plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],':',label='mu=0,sigma=3')
plt.plot(xs,[normal_cdf(x,mu=-2,sigma=2) for x in xs],'-.',label='mu=-2,sigma=3')
plt.legend(loc=5)
plt.title('Various Normal cdfs')
plt.show()