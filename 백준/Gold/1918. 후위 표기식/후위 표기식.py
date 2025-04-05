priority = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
answer = ""
for elm in input():
    if elm.isalpha():
        answer += elm
    elif elm == "(":
        stack.append(elm)
    elif elm == ")":
        while stack:
            temp = stack.pop()
            if temp == "(":
                break
            answer += temp
    else:
        while stack:
            temp = stack.pop()
            if temp == "(" or priority[temp] < priority[elm]:
                stack.append(temp)
                break
            answer += temp
        stack.append(elm)
while stack:
    answer += stack.pop()
print(answer)
