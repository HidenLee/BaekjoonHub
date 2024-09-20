for _ in range(int(input())):
    N , M = map(int,input().split())
    arr1 = sorted(list(map(int,input().split())))
    arr2 = sorted(list(map(int,input().split())))

    idx = 0
    ans = 0
    for elm in arr1:
        while idx < M and elm > arr2[idx]:
            idx += 1
        ans += idx
    print(ans)

