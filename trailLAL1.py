import sys
def last_digit(n):
    if n <= 1: return n
    prev, cur = 0, 1
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
        prev = prev % 10
        cur = cur % 10
    return cur

n = int(input())
print(last_digit(n))