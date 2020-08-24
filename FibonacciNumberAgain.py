import sys
def fibonacciAgain(n, m):
    if n <= 1:
        return n
    l1, l2, lengthCount, f = 0, 1, 0, [0, 1]
    for _ in range(2, (m * m) + 1):
        l3 = (l1 + l2) % m
        f.append(l3)
        l1, l2 = l2, l3
        lengthCount += 1
        if (l3 == 1) and (l1 == 0): break
    fRemainder = n % lengthCount
    return f[fRemainder]


n, m = input().split()
print(fibonacciAgain(int(n), int(m)))