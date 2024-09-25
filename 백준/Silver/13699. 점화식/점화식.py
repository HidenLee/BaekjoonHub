# https://www.acmicpc.net/problem/13699

arr = [1]*(int(input())+1)
for i in range(1,len(arr)):
    arr[i] = sum([arr[i-1-k]*arr[k] for k in range(i)])
print(arr[-1])