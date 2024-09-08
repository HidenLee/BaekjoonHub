N, X = map(int,input().split())
prefix_sum = [0]*(N+1)
for idx, ipt in enumerate(map(int,input().split())):
    prefix_sum[idx+1] = prefix_sum[idx] + ipt
ans = 0
cnt = 0
for i in range(X,N+1):
    temp = prefix_sum[i]-prefix_sum[i-X]
    if ans < temp:
        ans = temp
        cnt = 1
    elif ans == temp:
        cnt += 1
if ans:
    print(ans)
    print(cnt)

else:
    print("SAD")