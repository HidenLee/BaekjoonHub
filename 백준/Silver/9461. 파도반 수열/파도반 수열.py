a = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(100)]
T = int(input())
for test_case in range(T):
    N = int(input())
    left , right = 0 , 4
    while right < N:
        if not a[right+1]:
            a[right+1] = a[right] + a[left]
        right += 1
        left += 1
    print(a[N])