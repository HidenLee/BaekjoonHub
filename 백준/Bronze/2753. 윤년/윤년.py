# https://www.acmicpc.net/problem/2753 윤년
Y = int(input())
ans = 0
if not Y%4:
    if Y%100:
        ans = 1
    elif not Y%400:
        ans = 1
print(ans)