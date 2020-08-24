import sys
def optimalWeight(W, we):
    result = [[0 for i in range(W + 1)] for j in range(a + 1)]
    for totalItem in range(1, a + 1):
        for weight in range(1, W + 1):
            result[totalItem][weight] = result[totalItem - 1][weight]
            if we[totalItem - 1] <= weight:
                value = result[totalItem - 1][weight - we[totalItem - 1]] + we[totalItem - 1]
                if value > result[totalItem][weight]:
                    result[totalItem][weight] = value
    return result[a][W]
if __name__ == '__main__':
    input = sys.stdin.read()
    W, a, *we = list(map(int, input.split()))
    print(optimalWeight(W, we))