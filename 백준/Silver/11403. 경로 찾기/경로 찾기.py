def func2(mat1):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if mat1[i][k]*mat1[k][j]: 
                    mat1[i][j] = 1
                    break
    return mat1

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
for _ in range(N):
    lst = func2(lst)
for _ in range(N):
    print(*lst[_])