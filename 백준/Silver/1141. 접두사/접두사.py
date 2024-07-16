# https://www.acmicpc.net/problem/1141

def isAffix(big,small):
    if len(big) < len(small):
        return False
    for idx in range(len(small)):
        if small[idx] != big[idx]:
            return False
    else:
        return True


N = int(input())
arr =  [set() for _ in range(51)]
for _ in range(N):
    ipt = input()
    arr[len(ipt)].add(ipt)
ans = []
for idx in range(50,0,-1):
    for new in arr[idx]:
        for old in ans:
            if isAffix(old,new):
                break
        else:
            ans.append(new)
print(len(ans))