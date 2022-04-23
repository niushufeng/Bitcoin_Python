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

df = df[['datetime','Close']].set_index('datetime') # 设置索引
df.Close['2015-01-05 09:12:00']
#df

def return_(t): #函数
    
    x_num = [] #申请一个列表
    x_num.clear()
    for i in range(0,4000000):
        #x = i
        #return_BTC = math.log(df.Close[x + t]) - math.log(df.Close[x])
        #print(return_BTC)
        x = pd.to_datetime((df.index[i].timestamp() + t),unit='s')
        y = pd.to_datetime(df.index[i].timestamp(),unit='s')
        x_num.append(math.log(df.Close[x]) - math.log(df.Close[y])) #将数据读入列表
        #x_num[0:10]
    #count_(x_num) # 调用统计函数
    return x_num       
    #x_num1
    #return x_num1[0:100],y_num1[0:100]
    
    x_1 = return_(60*1)
x_2 = return_(60*2)
x_3 = return_(60*3)
x_4 = return_(60*4)
x_8 = return_(60*8)
x_16 = return_(60*16)
x_32 = return_(60*32)
x_64 = return_(60*64)
x_128 = return_(60*128)
x_256 = return_(60*256)
x_512 = return_(60*512)
x_1024 = return_(60*1024)
x_2048 = return_(60*2048)

x_1.remove(max(x_1))
x_1.remove(min(x_1))
x_2.remove(max(x_2))
x_2.remove(min(x_2))
x_3.remove(max(x_3))
x_3.remove(min(x_3))
x_4.remove(max(x_4))
x_4.remove(min(x_4))
x_8.remove(max(x_8))
x_8.remove(min(x_8))
x_16.remove(max(x_16))
x_16.remove(min(x_16))
x_32.remove(max(x_32))
x_32.remove(min(x_32))
x_64.remove(max(x_64))
x_64.remove(min(x_64))
x_128.remove(max(x_128))
x_128.remove(min(x_128))
x_256.remove(max(x_256))
x_256.remove(min(x_256))
x_512.remove(max(x_512))
x_512.remove(min(x_512))
x_1024.remove(max(x_1024))
x_1024.remove(min(x_1024))
x_2048.remove(max(x_2048))
x_2048.remove(min(x_2048))

frame = pd.DataFrame({'x_1':x_1})
frame.to_csv("x_1.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_2':x_2})
frame.to_csv("x_2.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_3':x_3})
frame.to_csv("x_3.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_4':x_4})
frame.to_csv("x_4.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_8':x_8})
frame.to_csv("x_8.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_16':x_16})
frame.to_csv("x_16.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_32':x_32})
frame.to_csv("x_32.csv",index = False , sep = ',')# index = False不写索引

frame = pd.DataFrame({'x_64':x_64})
frame.to_csv("x_64.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_128':x_128})
frame.to_csv("x_128.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_256':x_256})
frame.to_csv("x_256.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_512':x_512})
frame.to_csv("x_512.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_1024':x_1024})
frame.to_csv("x_1024.csv",index = False , sep = ',')

frame = pd.DataFrame({'x_2048':x_2048})
frame.to_csv("x_2048.csv",index = False , sep = ',')

