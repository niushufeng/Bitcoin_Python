plt.figure(figsize=(14,12), dpi=80)
plt.figure(1)

ax1 = plt.subplot(431)
ax1.plot(x_data_1, y_data_1, marker="o", markersize=7,  color="red", linestyle="--", label="$\Delta t = 1\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax2 = plt.subplot(432)
ax2.plot(x_data_2, y_data_2, marker="^", markersize=7,  color="darkgreen",  linestyle="--", label="$\Delta t = 2\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='best', fontsize=11, labelspacing=0.3, frameon=False)

ax3 = plt.subplot(433)
ax3.plot(x_data_3, y_data_3, marker="s", markersize=7,  color='#BB9727',     linestyle="--", label="$\Delta t = 3\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='best', fontsize=11, labelspacing=0.3, frameon=False)

ax4 = plt.subplot(434)
ax4.plot(x_data_4, y_data_4, marker="+", markersize=7,  color="blue",       linestyle="--", label="$\Delta t = 4\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax5 = plt.subplot(435)
ax5.plot(x_data_5, y_data_5, marker="*", markersize=7,  color='#05B9E2',     linestyle="--", label="$\Delta t = 8\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax6 = plt.subplot(436)
ax6.plot(x_data_7, y_data_7, marker="1", markersize=7,  color="#85618E",  linestyle="--", label="$\Delta t = 16\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax7 = plt.subplot(437)
ax7.plot(x_data_7, y_data_7, marker="4", markersize=7,  color="#4E587B", linestyle="--", label="$\Delta t = 32\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax8 = plt.subplot(438)
ax8.plot(x_data_8, y_data_8, marker="d", markersize=7,  color="#2F4858",   linestyle="--",label="$\Delta t = 64\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax9 = plt.subplot(439)
ax9.plot(x_data_9, y_data_9, marker="s", markersize=7,  color="saddlebrown",linestyle="--",label="$\Delta t = 128\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

ax10 = plt.subplot(4,3,10)
ax10.plot(x_data_10, y_data_10, marker="X", markersize=7,  color="#6CCEB5",linestyle="--",label="$\Delta t = 256\ min$")
plt.yscale('log') # 纵坐标转换
plt.xlabel('$G_{\Delta t}(t) = \ln S(t + \Delta t) - \ln S(t)$')
plt.ylabel('$\log_{10}P(G)/PDF$')
plt.legend(loc='upper right', fontsize=11, labelspacing=0.3, frameon=False)

plt.rcParams['axes.unicode_minus'] = False
plt.savefig('all_log-log.pdf',bbox_inches='tight')

plt.show()
