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
plt.xscale('log') # 纵坐标转换
plt.xlim(0.001,1)
u = 0
sigma = np.std(x_data_1)# 标准差
#sigma = sigma**2
x = np.linspace( u - 3*sigma, u + 3*sigma, 1000)
y = np.exp(-(x - u)**2 / (2 * sigma ** 2)) / ( np.sqrt(2 * np.pi) * sigma )
plt.xlabel('$\log_{10}G_{\Delta t}(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='best', fontsize=11, labelspacing=0.3, frameon=False)
plt.savefig('log-log.pdf',bbox_inches='tight')

plt.show()
#plt.plot(x,y,c="black", markersize=7, linestyle="-" )
sigma
