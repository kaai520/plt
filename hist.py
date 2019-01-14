import numpy as np
import matplotlib.pyplot as plt

#使用直方图，可以很容易看到数据的分布
np.random.seed(0)
mu,sigma=100,20  #标准差，方差
a = np.random.normal(mu,sigma,size=100)
# 参数20表示bin,即直方图的个数；normed=1表示概率，normed=0表示出现的个数
plt.hist(a,30,normed=0,histtype='stepfilled',facecolor='b',alpha=0.75)
plt.title('Histogram')
plt.show()
