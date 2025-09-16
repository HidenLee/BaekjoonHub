def solution(s):
    answer = 0
    dic = {"[":"]","{":"}","(":")"}
    for idx in range(len(s)):
        count = 0
        stack = []
        flag = True
        while count < len(s) and flag:
            elm = s[(idx+count)%len(s)]
            if elm in ["[","{","("]:
                stack.append(elm)
            else:
                if stack and dic[stack[-1]] == elm:
                    stack.pop()
                else:
                    flag = False
                    break
            count += 1
        answer += 1 if flag and not stack else 0
    return answer

