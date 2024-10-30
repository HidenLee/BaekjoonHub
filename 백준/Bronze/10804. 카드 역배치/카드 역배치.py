arr = [i for i in range(21)]
for a,b in [map(int,input().split()) for _ in range(10)]:
    arr = arr[:a] + arr[a:b+1][::-1] + arr[b+1:]
print(*arr[1:])
