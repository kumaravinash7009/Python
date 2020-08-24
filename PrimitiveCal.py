import sys
def optimalSequence(n):
    c = [0] * (n + 1)
    if n == 1: 
        return[0, [1]]
    for i in range(2, n + 1):
        value1 = c[i - 1] + 1
        value2 = c[i // 2] + 1 if i % 2 == 0 else float("inf")
        value3 = c[i // 3] + 1 if i % 3 == 0 else float("inf")
        sp = min(value1, value2, value3)
        c[i] = c[i - 1] + 1 if sp == value1 else c[i // 2] + 1 if sp == value2 else c[i // 3] + 1
    return [c[n], writeSequence(n, c)]
def writeSequence(n,c):
    j, seq = n, [n]
    while j > 1:
        value1 = c[j - 1] + 1
        value2 = c[j // 2] + 1 if j % 2 == 0 else float("inf")
        value3 = c[j // 3] + 1 if j % 3 == 0 else float("inf")
        fp = min(value1, value2, value3)
        if (fp == value1):
            seq.append(j - 1)
            j -= 1
        elif(fp == value2):
            seq.append(j // 2)
            j //= 2
        elif (fp == value3):
            seq.append(j // 3)
            j //= 3
    return reversed(seq)
input = sys.stdin.read()
n = int(input)
[num, seq] = (optimalSequence(n))
print(num)
for x in seq:
    print(x, end=' ')