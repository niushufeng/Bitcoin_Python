u1 = max(hist_1)
u2 = max(hist_2)
u3 = max(hist_3)
u4 = max(hist_4)
u8 = max(hist_5)
u16 = max(hist_6)
u32 = max(hist_7)
u64 = max(hist_8)
u128 = max(hist_9)
u256 = max(hist_10)
u512 = max(hist_11)
u1024 = max(hist_12)
u2048 = max(hist_13)

y = [u1,u2,u3,u4,u8,u16,u32,u64,u128,u256,u512,u1024,u2048]

x = [1,2,3,4,8,16,32,64,128,256,512,1024,2048]

plt.scatter(x,y)
#plt.plot(x1,a1*x1+b1)
#plt.ylim(10,100)
#plt.plot(x, y1)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('$\Delta t (s)$')
plt.ylabel('$P(0)$')
plt.savefig('scatter.pdf',bbox_inches='tight')

plt.show()
