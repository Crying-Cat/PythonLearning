import numpy as np
import matplotlib.pyplot as plt

def normpdf(x,mu,sigma):
    return 1/np.sqrt(2*np.pi)/sigma*np.exp(-(x-mu)**2/2/sigma**2)

sample = np.random.randn(10000)
print(sample.shape)
plt.hist(sample,30)
plt.show()

# 计算似然
sigmas = np.linspace(0.8,1.2,100)
likelihood = np.zeros(sigmas.size)
for i in range(sigmas.size):
    p = normpdf(sample,0,sigmas[i])*4
    likelihood[i] = np.prod(p)

plt.plot(sigmas,likelihood)
plt.show()