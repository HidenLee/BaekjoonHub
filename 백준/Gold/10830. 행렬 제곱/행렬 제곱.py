#https://www.acmicpc.net/problem/10830 행렬 제곱

def pprint(lst):
    for _ in range(len(lst)):
        print(*lst[_])


def comb(A,B):
    ret = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = sum([A[i][t]*B[t][j] for t in range(N)])%1000
    return ret

def func(mat,n):
    if n == 1:
        return mat
    if n % 2:
        return comb(func(mat,n-1),mat)
    halfn =  n // 2
    return func(comb(mat,mat),halfn)

def div_int(a):
    return int(a)%1000

N, B = map(int, input().split())
matrix = [list(map(div_int, input().split())) for _ in range(N)]
pprint(func(matrix,B))