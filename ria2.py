import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 0.00001)

k=2
y = x**k

y2=[0]
total=0
for i in range(0,1000000):
    _x=i*0.00001
    _x2=(i+1)*0.00001
    n=(_x+_x2)/2
    f=(lambda x:(k*n**(k-1))*(x-n)+n**k)
    #plt.hlines(v_y, i, i+1, color='blue', linestyle='solid', linewidth=1)
    y2.append(f(_x2))
    #plt.vlines(i, 0, f(i), color='blue', linestyle='solid', linewidth=1)
    #plt.vlines(i+1, 0, f(i+1), color='blue', linestyle='solid', linewidth=1)
    total+=(f(_x)+f(_x2))/2*0.00001

print(total)
#plt.plot(x, y, "red")
#plt.plot([i for i in range(11)],y2,"blue")
#plt.show()