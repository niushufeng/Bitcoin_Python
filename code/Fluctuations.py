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

df_1 = df1.reset_index(inplace=False,drop=False)  
df_1['index'] = df_1['index'] * 60 + 1365696060
df_1['datetime'] = pd.to_datetime(df_1['index'],unit='s')
#df11 = df11[['datetime','x_1']].set_index('datetime') # 设置索引
plt.plot(df_1.datetime,df_1['x_1'])
plt.xlabel('Time')
plt.ylabel('Fluctuations')
plt.savefig('Fluctuations.pdf',bbox_inches='tight')

plt.show()
