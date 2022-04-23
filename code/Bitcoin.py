import pandas as pd
import numpy as np
import datetime,time
import math
import matplotlib.pyplot as plt
from numpy import nan as NaN
from scipy import stats #绘图
import seaborn as sns
from collections import Counter # 统计函数
from scipy.stats import *
from numpy.random import randn
import matplotlib as mpl

mpl.rcParams.update(
{
 'text.usetex': False,
 'font.family': 'stixgeneral',
 'mathtext.fontset':'stix',
}
)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#plt.rcParams['figure.figsize'] = (10.0,8.0)
#plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'
#plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\bitcon.csv',encoding = 'gbk')
df = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\bitcon.csv')
df['datetime'] = pd.to_datetime(df['Timestamp'],unit='s')
df = df[['datetime','Close']].set_index('datetime') # 设置索引
df = df[df.index > pd.to_datetime("2013-04-12 00:01:00")]
df.describe()
df = df.reset_index()
df
b = pd.DataFrame()
b['datetime'] = pd.date_range(start='2013-04-12 00:02:00', end='2021-03-31 00:00:00',freq='Min') # freq指频率
b['Close'] = np.nan
b
df = df.append(b)
df = df.drop_duplicates(subset = ['datetime']).sort_values(by = ['datetime']).reset_index(drop=True)
df['Close'].fillna(method = 'ffill',inplace = True) #用上一个值覆盖空值
df.reset_index()['datetime'].diff().describe()

plt.plot(df.datetime,df.Close)
#plt.title('Daily number of trade price in Bitcoin')
#year = [str(i)+ '年' for i in range(2013,2021) ]
    # Creating legend with loc="best" can be slow with large amounts of data.
plt.xlabel('Time')
plt.ylabel('Daily number of trade price in Bitcoin($)')
#plt.tight_layout()
#plt.savefig(r'60.jpg',bbox_inches='tight')
plt.legend(('Bitcoin',),loc='best')
plt.rcParams['axes.unicode_minus'] = False
plt.savefig('trade_2013-2021.pdf',bbox_inches='tight')

#plt.figure(figsize = (20,12))

plt.show()
