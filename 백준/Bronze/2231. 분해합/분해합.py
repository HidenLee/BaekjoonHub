n = int(input())
for i in range(max(1, n - 9 * len(str(n))), n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)
