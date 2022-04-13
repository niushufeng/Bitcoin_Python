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


# In[6]:


df.reset_index()['datetime'].diff().describe()


# In[7]:


df.head(10)


# In[8]:


df.shape #行数和列数


# In[9]:


df[912070:912080]


# In[10]:


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


# In[11]:


df = df[['datetime','Close']].set_index('datetime') # 设置索引
df.Close['2015-01-05 09:12:00']
df


# In[112]:


x_num = [] #申请一个列表
y_num = list()
def return_(t): #函数
    x_num.clear()
    
    for i in range(0,40000):
        #x = i
        #return_BTC = math.log(df.Close[x + t]) - math.log(df.Close[x])
        #print(return_BTC)
        x = pd.to_datetime((df.index[i].timestamp() + t),unit='s')
        y = pd.to_datetime(df.index[i].timestamp(),unit='s')
        x_num.append(math.log(df.Close[x]) - math.log(df.Close[y])) #将数据读入列表
        x_num[0:10]
        number = x_num
    #count_(x_num) # 调用统计函数
    return        
    #x_num1
    #return x_num1[0:100],y_num1[0:100]


# In[181]:


return_(60*1000)


# In[182]:


result = Counter(x_num)
x_num1 = list(result.keys())
y_num1 = list(result.values())
new_y = [i/40000 for i in y_num1]
y_num1 = new_y
x = x_num1
y = y_num1
data = result.items()
df1 = pd.DataFrame(data,columns=['x', 'y']) #将x,y设置成数据流
df1 = df1.set_index('x') 
df1 = df1.sort_index()
x = list(df1.index)
y = list(df1['y'])


# In[183]:


df1.index


# In[184]:


#plt.yscale('log') # 纵坐标转换
plt.plot(x,new_y)
plt.scatter(x,new_y)
plt.show()


# In[185]:


sns.distplot(x,label = '1000min',hist = True,kde_kws={'color':'#098154','label':'1000min'},kde = True)#,fit = gamma) # 拟合正太分布,gamma分布
plt.scatter(x,new_y)
plt.yscale('log') # 纵坐标转换

plt.title('$\log-returns$')
plt.xlabel('$G_\Delta(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)$')
#plt.tight_layout()
#plt.savefig(r'60.jpg',bbox_inches='tight')
plt.savefig('1000min.pdf',bbox_inches='tight')
plt.rcParams['axes.unicode_minus'] = False
plt.legend()

plt.show()


# In[159]:


#sns.distplot(x_num1,label = '1min',hist = False,kde_kws={'color':'#098154'})
#plt.yscale('log') # 纵坐标转换
#sns.pairplot(tips = df1.y)
#plt.show()


# In[ ]:


#sns.distplot(x_num1,label = '1min',hist = False,kde_kws={'color':'#098154'})
#plt.yscale('log') # 纵坐标转换
#sns.pairplot(tips = df1.y)
#plt.show()


# $$a^2$$

# Levy stable:
# $$L_\alpha(Z,\Delta t) \equiv \frac{1}{\pi}\int_{0}^{\infty } exp(-\gamma \Delta t q^\alpha)\cos(qZ) \,dq$$

# $$P(0) \equiv L_\alpha(0,\Delta t) = 
#  \frac{\varGamma (1/ \alpha)}{\pi \alpha(\gamma \Delta t)^{1/ \alpha}} $$

# $$G_\Delta(t) = \ln S(t + \Delta t) - \ln S(t)$$

# $$R_t = \log P_t - \log P_{t- \Delta t}$$

# $$R_t ^ {norm} = \frac{R_t - \mu_R}{\sigma_R}$$

# In[17]:


import os 
print(sns.distplot.__code__)


# In[124]:


get_ipython().run_line_magic('pinfo', 'sns.distplot')


# In[19]:


sns.stripplot(x,y)# 费cpu


# In[ ]:




