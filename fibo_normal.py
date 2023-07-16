from os import system
system("color f0")
a = [1, 1] #a_1=1, a_2=1
n = 10

for i in range(2, n):
    a_i = a[i-1]+a[i-2] #a_n=a_n-1 + a_n-2
    a.append(a_i)

[print(f"{i+1}번째\t{a[i]}") for i in range(len(a))]
