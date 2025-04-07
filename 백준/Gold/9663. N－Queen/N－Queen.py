N = int(input())
cnt = 0
for i in range(N):
    stack = [[i]]
    while stack:
        arr = stack.pop()
        if len(arr) == N:
            cnt += 1
            continue
        for j in range(N):
            for idx,k in enumerate(arr):
                if j == k:
                    break
                if len(arr) - idx == abs(k-j):
                    break
            else:
                stack.append(arr+[j])
print(cnt)

