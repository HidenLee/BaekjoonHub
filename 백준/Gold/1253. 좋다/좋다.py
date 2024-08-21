N = int(input())
srtarr = sorted(list(map(int,input().split())))
goodset = set()
ans = 0
for i in range(N):
    target = srtarr[i]
    if target in goodset:
        ans += 1
        continue
    left, right = 0, N-1
    while left < right:
        if left == i :
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if target < srtarr[left] + srtarr[right]:
            right -= 1
        elif target > srtarr[left] + srtarr[right]:
            left += 1
        else:
            ans += 1
            goodset.add(srtarr[left] + srtarr[right])
            break
print(ans)
