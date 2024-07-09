# https://www.acmicpc.net/problem/10799

right = 0
cnt = 0
flag = False
for b in input():
    if b == ")":
        if flag:
            right -= 1
            cnt += right
        else:
            right -= 1
            cnt += 1
        flag = False
        
    else:
        right += 1
        flag = True
print(cnt+right)