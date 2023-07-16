import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 0.1)
y =  x**10
y2=[0]

total=0
for i in range(0,10):
    n1=(i)*10
    n2=(i+1)*10
    v_y=(y[n1]+y[n2])/2
    y2.append(y[n2])
    #plt.hlines(v_y, i, i+1, color='blue', linestyle='solid', linewidth=1)
    plt.vlines(i, 0, y[n1], color='blue', linestyle='solid', linewidth=1)
    plt.vlines(i+1, 0, y[n2], color='blue', linestyle='solid', linewidth=1)
    total+=(y[n1]+y[n2])/2

print(total)
plt.plot(x, y, "red")
plt.plot([i for i in range(11)],y2,"blue")
plt.show()