def solution(s):
    flag = 0
    if len(s) % 2:
        return False
    for elm in s:
        if elm == "(":
            flag += 1
        else:
            flag -= 1
            if flag < 0:
                return False
    else:
        if flag:
            return False
                
    return True