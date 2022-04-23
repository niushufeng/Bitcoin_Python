import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from scipy import stats #绘图
from numpy.random import randn
import matplotlib as mpl
import sys

mpl.rcParams.update(
{
 'text.usetex': False,
 'font.family': 'stixgeneral',
 'mathtext.fontset':'stix',
}
)

#plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#plt.rcParams['figure.figsize'] = (10.0,8.0)
#plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'
#plt.rcParams['axes.unicode_minus'] = False

df1 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_1.csv')
df2 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_2.csv')
df3 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_3.csv')
df4 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_4.csv')
df5 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_8.csv')
df6 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_16.csv')
df7 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_32.csv')
df8 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_64.csv')
df9 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_128.csv')
df10 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_256.csv')
df11 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_512.csv')
df12 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_1024.csv')
df13 = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\sys\x_2048.csv')

hist_1, bins_1 = np.histogram(df1['x_1'], bins=50, density=True)
hist_2, bins_2 = np.histogram(df2['x_2'], bins=50, density=True)
hist_3, bins_3 = np.histogram(df3['x_3'], bins=50, density=True)
hist_4, bins_4 = np.histogram(df4['x_4'], bins=50, density=True)
hist_5, bins_5 = np.histogram(df5['x_8'], bins=50, density=True)
hist_6, bins_6 = np.histogram(df6['x_16'], bins=50, density=True)
hist_7, bins_7 = np.histogram(df7['x_32'], bins=50, density=True)
hist_8, bins_8 = np.histogram(df8['x_64'], bins=50, density=True)
hist_9, bins_9 = np.histogram(df9['x_128'], bins=50, density=True)
hist_10, bins_10 = np.histogram(df10['x_256'], bins=50, density=True)
hist_11, bins_11 = np.histogram(df11['x_512'], bins=50, density=True)
hist_12, bins_12 = np.histogram(df12['x_1024'], bins=50, density=True)
hist_13, bins_13 = np.histogram(df13['x_2048'], bins=50, density=True)

y_data_1 = hist_1.copy()
y_data_2 = hist_2.copy()
y_data_3 = hist_3.copy()
y_data_4 = hist_4.copy()
y_data_5 = hist_5.copy()
y_data_6 = hist_6.copy()
y_data_7 = hist_7.copy()
y_data_8 = hist_8.copy()
y_data_9 = hist_9.copy()
y_data_10 = hist_10.copy()
#y_data_11 = hist_11.copy()
#y_data_12 = hist_12.copy()
#y_data_13 = hist_13.copy()

x_data_1 = (bins_1[1:bins_1.size] + bins_1[0:bins_1.size-1])/2.0
x_data_2 = (bins_2[1:bins_2.size] + bins_2[0:bins_2.size-1])/2.0
x_data_3 = (bins_3[1:bins_3.size] + bins_3[0:bins_3.size-1])/2.0
x_data_4 = (bins_4[1:bins_4.size] + bins_4[0:bins_4.size-1])/2.0
x_data_5 = (bins_5[1:bins_5.size] + bins_5[0:bins_5.size-1])/2.0
x_data_6 = (bins_6[1:bins_6.size] + bins_6[0:bins_6.size-1])/2.0
x_data_7 = (bins_7[1:bins_7.size] + bins_7[0:bins_7.size-1])/2.0
x_data_8 = (bins_8[1:bins_8.size] + bins_8[0:bins_8.size-1])/2.0
x_data_9 = (bins_9[1:bins_9.size] + bins_9[0:bins_9.size-1])/2.0
x_data_10 = (bins_10[1:bins_10.size] + bins_10[0:bins_10.size-1])/2.0
#x_data_11 = (bins_11[1:bins_11.size] + bins_11[0:bins_11.size-1])/2.0
#x_data_12 = (bins_12[1:bins_12.size] + bins_12[0:bins_12.size-1])/2.0
#x_data_13 = (bins_13[1:bins_13.size] + bins_13[0:bins_13.size-1])/2.0

plt.plot(x_data_1, y_data_1, marker="*", markersize=7,  color="red", linestyle="--", label="$\Delta t = 1\ min$")
plt.plot(x_data_2, y_data_2, marker="^", markersize=7,  color="darkgreen", linestyle="--", label="$\Delta t = 2\ min$")
plt.plot(x_data_3, y_data_3, marker="v", markersize=7,  color='#ED9F54', linestyle="--", label="$\Delta t = 3\ min$")
plt.plot(x_data_4, y_data_4, marker="+", markersize=7,  color="#E57B71", linestyle="--", label="$\Delta t = 4\ min$")
plt.plot(x_data_5, y_data_5, marker="o", markersize=7,  color='#BE688A',  linestyle="--", label="$\Delta t = 8\ min$")
plt.plot(x_data_6, y_data_6, marker="1", markersize=7,  color="#85618E",  linestyle="--", label="$\Delta t = 16\ min$")
plt.plot(x_data_7, y_data_7, marker="4", markersize=7,  color="#4E587B", linestyle="--", label="$\Delta t = 32\ min$")
plt.plot(x_data_8, y_data_8, marker="d", markersize=7,  color="#2F4858",   linestyle="--",label="$\Delta t = 64\ min$")
plt.plot(x_data_9, y_data_9, marker="s", markersize=7,  color="saddlebrown",linestyle="--",label="$\Delta t = 128\ min$")
plt.plot(x_data_10, y_data_10, marker="X", markersize=7,  color="#6CCEB5",linestyle="--",label="$\Delta t = 256\ min$")
plt.yscale('log') # 纵坐标转换
#plt.xscale('log')

plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.rcParams['axes.unicode_minus'] = False
plt.legend(loc='best', fontsize=11, labelspacing=0.3, frameon=False)
plt.savefig('1-2048(400).pdf',bbox_inches='tight')

plt.show()
