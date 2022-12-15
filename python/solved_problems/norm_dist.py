from numpy import random as rnd
from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

data = rnd.normal(0, 1, 10000)
index = np.arange(data.shape[0])
stats.probplot(data, dist="norm", plot=plt)
plt.show()
plt.plot(index, data)
plt.show()
plt.hist(data)
plt.show()
uniform_data = rnd.uniform(size=1000)
stats.probplot(uniform_data, dist="norm", plot=plt)
plt.show()