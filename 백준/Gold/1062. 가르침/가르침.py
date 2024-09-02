# https://www.acmicpc.net/problem/1062
def ipt(str1):
    temp = ["0" for _ in range(26)]
    for elm in str1:
        # print(ord(elm)-97)
        temp[ord(elm)-97] = "1"
    return int("".join(temp),2)

def func1(case):
    cnt = 0
    for word in arr:
        if word & case == word:
            cnt += 1
    return cnt

def backtrack(idx, learned, selected):
    global ans
    if selected == K - 5:
        ans = max(ans,func1(learned))
        return
    for i in range(idx,26):
        if not learned & (1 << i):
            backtrack(i+1, learned| (1<<i),selected+1)

N ,K = map(int,input().split())
arr = [ipt(input()) for _ in range(N)]
ans = 0
if K < 5 :
    print(0)
else:
    learned = ipt("antic")
    backtrack(0,learned,0)
    print(ans)