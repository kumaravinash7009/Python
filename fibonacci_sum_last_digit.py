
def fibonacciSum(n):
    if n <= 1: 
        return n
    prev, cur, sum, nRemainder = 0, 1, 1, n % 60
    if (nRemainder == 0) or (nRemainder == 1): return nRemainder
    for _ in range(nRemainder - 1):
        prev, cur = cur % 10, prev % 10 + cur % 10
        sum = (sum + cur % 10) % 10
    return sum

n = int(input())
print(fibonacciSum(n))