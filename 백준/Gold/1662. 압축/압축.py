# https://www.acmicpc.net/problem/1662
ipt = input()
flag = False
ans = 0
stack = [0]
for elm in ipt[::-1]:
    if elm == ")":
        stack.append(0)
    elif elm == "(":
        flag = True
    else:
        if flag:
            temp = stack.pop()
            stack[-1] += temp * int(elm)
        else:
            stack[-1] += 1
        flag = False
print(stack[0])