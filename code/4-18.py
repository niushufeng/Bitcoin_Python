#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


# df = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\bitcon.csv',encoding = 'gbk')
df = pd.read_csv(r'C:\Users\niushuchao\Desktop\A\bitcon.csv')
df['datetime'] = pd.to_datetime(df['Timestamp'],unit='s')
df = df[['datetime','Close']].set_index('datetime') # 设置索引
df = df[df.index > pd.to_datetime("2013-04-12 00:01:00")]
df.describe()


# In[3]:


df = df.reset_index()
df


# In[4]:


b = pd.DataFrame()
b['datetime'] = pd.date_range(start='2013-04-12 00:02:00', end='2021-03-31 00:00:00',freq='Min') # freq指频率
b['Close'] = np.nan
b


# In[5]:


df = df.append(b)
df = df.drop_duplicates(subset = ['datetime']).sort_values(by = ['datetime']).reset_index(drop=True)
df['Close'].fillna(method = 'ffill',inplace = True) #用上一个值覆盖空值
df.reset_index()['datetime'].diff().describe()


# In[6]:


df.head(10)


# In[7]:


df.shape #行数和列数


# In[8]:


df[912070:912080] # 查看缺失是否补上


# In[9]:


plt.plot(df.datetime,df.Close,color = 'g',)
#plt.title('Daily number of trade price in Bitcoin')
#year = [str(i)+ '年' for i in range(2013,2021) ]
    # Creating legend with loc="best" can be slow with large amounts of data.
plt.xlabel('Datetime')
plt.ylabel('Daily number of trade price in Bitcoin($)')
#plt.tight_layout()
#plt.savefig(r'60.jpg',bbox_inches='tight')
plt.savefig('trade_2013-2021.pdf',bbox_inches='tight')
plt.rcParams['axes.unicode_minus'] = False
#plt.figure(figsize = (20,12))
plt.legend(('Bitcoin',),loc='best')
plt.show()


# In[10]:


df = df[['datetime','Close']].set_index('datetime') # 设置索引
df.Close['2015-01-05 09:12:00']
df


# In[11]:


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


# In[12]:


x_1 = return_(60*1)


# In[149]:


x_5 = return_(60*5)


# In[175]:


x_10 = return_(60*10)


# In[190]:


x_100 = return_(60*100)


# In[225]:


x_1day = return_(60*1440)


# In[28]:





# In[ ]:


x_1.remove(max(x_1))
x_1.remove(min(x_1))
x_5.remove(max(x_5))
x_5.remove(min(x_5))
x_10.remove(max(x_10))
x_10.remove(min(x_10))
x_100.remove(max(x_100))
x_100.remove(min(x_100))
x_1day.remove(max(x_1day))
x_1day.remove(min(x_1day))


# In[187]:


frame = pd.DataFrame({'x_1':x_1})
frame.to_csv("x_1.csv",index = False , sep = ',')


# In[188]:


frame = pd.DataFrame({'x_5':x_5})
frame.to_csv("x_5.csv",index = False , sep = ',')


# In[197]:


frame = pd.DataFrame({'x_10':x_10})
frame.to_csv("x_10.csv",index = False , sep = ',')# index = False不写索引


# In[222]:


frame = pd.DataFrame({'x_100':x_100})
frame.to_csv("x_100.csv",index = False , sep = ',')


# In[231]:


frame = pd.DataFrame({'x_1day':x_1day})
frame.to_csv("x_1day.csv",index = False , sep = ',')


# In[273]:


sns.kdeplot(x_1, shade=False, bw=0.005, color="c",linestyle='-',marker=r'v',label='$\Delta t$= 1min') #核密度
sns.kdeplot(x_5, shade=False, bw=0.01, color="b",linestyle='-',marker=r'^',label='$\Delta t$= 5min') #核密度
sns.kdeplot(x_10, shade=False, bw=0.01, color="r",linestyle='-',marker=r'<',label='$\Delta t$= 10min') #核密度
sns.kdeplot(x_100, shade=False, bw=0.0135, color='m',linestyle='-',marker=r'>',label='$\Delta t$= 100min') #核密度
sns.kdeplot(x_1day, shade=False, bw=0.011, color='#B22222',cut=0,linestyle='-',marker=r'+',label='$\Delta t$= 1day') #核密度
plt.yscale('log') # 纵坐标转换

plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.savefig('1-1440(400w).pdf',bbox_inches='tight')
plt.rcParams['axes.unicode_minus'] = False
plt.legend(loc='best')

plt.show()


# In[215]:


plt.plot(x_100) # 2013年收益率波动大，中间


# In[271]:


counts, rets = np.histogram(x_1) 
rets = rets[:-1] + (rets[1] - rets[0])/2 
freqs = 1.0/(counts + 0.01) 
freqs = np.log(freqs)


# In[272]:


p = np.polyfit(rets,freqs, 1)
plt.plot(rets, freqs, 'o') 
plt.plot(rets, p[0] * rets + p[1]) 
plt.show()


# In[270]:


#sns.kdeplot(x_100, shade=False, bw=.0135, color="g",cut=3,cumulative=False,linestyle='-',marker=r'v',label='1min') #核密度 cut 指切除带宽往数轴极限数值的多少(默认为3) cumulative,绘制累积分布
sns.kdeplot(x_1, shade=False, bw=0.005, color="c",linestyle='-',marker=r'v',label='$\Delta t$= 1min') #核密度
#sns.kdeplot(x_5, shade=False, bw=0.01, color="b",linestyle='-',marker=r'^',label='$\Delta t$= 5min') #核密度
#sns.kdeplot(x_10, shade=False, bw=0.01, color="r",linestyle='-',marker=r'<',label='$\Delta t$= 10min') #核密度
#sns.kdeplot(x_100, shade=False, bw=0.0135, color='m',linestyle='-',marker=r'>',label='$\Delta t$= 100min') #核密度
#sns.kdeplot(x_1day, shade=False, bw=0.011, color='#B22222',cut=0,linestyle='-',marker=r'+',label='$\Delta t$= 1day') #核密度

plt.yscale('log') # 纵坐标转换

plt.xlabel('$G_\Delta(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.savefig('1(400w).pdf',bbox_inches='tight')
plt.rcParams['axes.unicode_minus'] = False
plt.legend(loc='upper left')

plt.show()


# $$a^2$$

# Levy stable:
# $$L_\alpha(Z,\Delta t) \equiv \frac{1}{\pi}\int_{0}^{+\infty } \exp(-\gamma \Delta t q^\alpha)\cos(qZ) \,dq$$

# Gamma函数
# 
# $$\varGamma (t) = \int_{0}^{+\infty} x^{t-1} e^{-x} dx(t>0)$$

# $$P(0) \equiv L_\alpha(0,\Delta t) = 
#  \frac{\varGamma (1/ \alpha)}{\pi \alpha(\gamma \Delta t)^{1/ \alpha}} $$

# $$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$$

# $$R_t = \log P_t - \log P_{t- \Delta t}$$

# $$R_t ^ {norm} = \frac{R_t - \mu_R}{\sigma_R}$$

# 幂律分布就是概率密度函数服从幂函数的分布，幂律分布公式:
# $$Y = aX^{-b}$$
# 
# $$\log Y = \log aX^{-b} = \log a - b \log X$$
# 
# 令
# $$y = \log Y , x = \log X ， y = c - bx$$
# 
# 对于幂律公式，对X,Y取对数后，在坐标轴上为线性方程

# In[ ]:




