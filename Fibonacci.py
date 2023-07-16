import matplotlib.pyplot as plt

seq = [1, 1]


def fib(n):
    global seq
    m = n - 1
    if m < len(seq):
        return seq[m]
    for i in range(len(seq), n):
        a_i = seq[i-1]+seq[i-2]
        seq.append(a_i)
    return seq[m]


i = 1
b_value = 0
stack = 0

seq2 = []

while True:
    value = fib(i+1)/fib(i)
    seq2.append(value)
    if b_value == value:
        stack += 1
    else:
        stack = 0
    if stack > 5:
        break
    print(i, "\t", value)
    b_value = value
    i += 1

plt.plot([i+1 for i in range(0, len(seq2))], seq2)
plt.show()
