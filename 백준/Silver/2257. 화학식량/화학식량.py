dic = { x:int(x) if x.isdigit() else 1 if x=="H" else 12 if x=="C" else 16 if x=="O" else x for x in list(map(str,range(2,10)))+["H","C","O","(",")"]}
ipt = [ dic[x] for x in list(input())]
idx = 0
# print(ipt)

stack = []
while idx < len(ipt):
    if ipt[idx] in range(2,10):
        stack[-1] *= ipt[idx]
    elif ipt[idx] == "(":
        stack.append("(")
    elif ipt[idx] == ")":
        temp = 0
        while stack[-1] != "(":
            temp += stack.pop()
        stack.pop()  # Remove the "("
        stack.append(temp)
    
    else:
        stack.append(ipt[idx])
    idx += 1
print(sum(stack))