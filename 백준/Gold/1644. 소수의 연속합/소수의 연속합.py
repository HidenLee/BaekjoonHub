def eratos(N):
    arr = [True] * (N + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(N**0.5) + 1):
        if arr[i]:
            for j in range(i * i, N + 1, i):
                arr[j] = False
    
    return [i for i in range(N + 1) if arr[i]]

def solve():
    N = int(input())
    arr = eratos(N)
    left = right = total = ans = 0
    while True:
        if total == N:
            ans += 1
        if total > N:
            total -= arr[left]
            left += 1
        else:
            if right == len(arr):
                break
            total += arr[right]
            right += 1
    print(ans)
solve()