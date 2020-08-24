
def editDis(a, b):
    lista, listb = [0]+ [x for x in a], [0]+ [y for y in b]
    n, m = len(lista), len(listb)
    d = [[0 for x in range(m)] for y in range(n)]
    for i in range(n): d[i][0] = i
    for j in range(m): d[0][j] = j
    for j in range(1, m):
        for i in range(1, n):
            insert = d[i][j - 1] + 1
            delete = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if lista[i] == listb[j]:
                d[i][j] = min(insert, delete, match)
            else:
                d[i][j] = min(insert, delete, mismatch)
    return d[n - 1][m - 1]
if __name__ == "__main__":
    print(editDis(input(), input()))