x_1 = return_(60*1)
x_2 = return_(60*2)



x_1.remove(max(x_1))
x_1.remove(min(x_1))
x_2.remove(max(x_2))
x_2.remove(min(x_2))
x_5.remove(max(x_5))
x_5.remove(min(x_5))
x_10.remove(max(x_10))
x_10.remove(min(x_10))
x_100.remove(max(x_100))
x_100.remove(min(x_100))
x_1day.remove(max(x_1day))
x_1day.remove(min(x_1day))

frame = pd.DataFrame({'x_1':x_1})
frame.to_csv("x_1.csv",index = False , sep = ',')
frame = pd.DataFrame({'x_2':x_2})
frame.to_csv("x_2.csv",index = False , sep = ',')
frame = pd.DataFrame({'x_5':x_5})
frame.to_csv("x_5.csv",index = False , sep = ',')
frame = pd.DataFrame({'x_10':x_10})
frame.to_csv("x_10.csv",index = False , sep = ',')# index = False不写索引
frame = pd.DataFrame({'x_100':x_100})
frame.to_csv("x_100.csv",index = False , sep = ',')
frame = pd.DataFrame({'x_1day':x_1day})
frame.to_csv("x_1day.csv",index = False , sep = ',')

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

plt.plot(x_100) # 2013年收益率波动大，中间

