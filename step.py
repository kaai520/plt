import matplotlib.pyplot as plt
import numpy as np

year=np.array([1991,1995,1999,2001,2002,2006,2007,2008,2009,2010])
price=np.array([0.29,0.32,0.33,0.34,0.37,0.39,0.41,0.42,0.44,0.44])
year_10=year+10

fig,ax=plt.subplots(figsize=(10,15))

ax.step(year,price,where='post',color='r')
ax.step(year_10,price,where='post',color='b')
ax.set_title("US Postage Fee") #设置标题
ax.set_xticks(year) #设置x轴刻度
#去除边框
ax.spines["top"].set_visible(False)
# ax.spines["bottom"].set_visible(False)
# ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
#添加文字注释
for i,j in zip(year,price):
    ax.text(x=i,y=j+0.003,s=j)
for i,j in zip(year_10,price):
    ax.text(x=i, y=j + 0.003, s=j)

plt.show()

