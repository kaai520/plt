import matplotlib.pyplot as plt

# 标签
labels = ['chinese', 'math', 'english']
# 这里并不表示比例，只是表示相对大小，真正的比例它会自动计算
sizes = [10, 20, 100]
# 这里表示突出的程度
explode = (0, 0, 0.1)
# autopct 比例的显示精度，shadow阴影，startangle起始角度
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#正圆
plt.axis('equal')
plt.show()
