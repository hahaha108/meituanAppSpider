# import os

import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

labels = u'深圳', u'北京', u'上海', u'广州',u'襄阳'  # 设置标签
sizes = [23540, 24964, 28380, 21709, 2851]  # 占比，和为100
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red']  # 颜色
explode = (0, 0, 0, 0,0.1)  # 展开间距为0.1

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
        startangle=90)  # startangle控制饼状图的旋转方向
plt.axis('equal')  # 保证饼状图是正圆，否则会有一点角度偏斜

plt.show()
