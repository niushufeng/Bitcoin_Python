from sklearn.linear_model import LinearRegression
#定义我们的x值和y值：
#x = data["Daily_flow_of_people(k)"].values.reshape(-1,1)
#y = data[“Daily_sales_revenue(k_yuan)”].values.reshape(-1,1)
#建立Regression的模型：
x1 = np.array(x)
y1 = np.array(y)
x1 = x1.reshape(-1,1)
y1 = y1.reshape(-1,1)

reg = LinearRegression()
model = reg.fit(x1, y1)

#然后就可以查看这个线性方程y=ax+b的系数和截距值了。

#查看截距（intercept是截距的意思，也就是b）：
b1 = model.intercept_

#查看系数（coefficient是系数的意思，也就是a）：
a1 = model.coef_
#y1 = a1 * x1 + b1
plt.plot(x, y1)
plt.show()
