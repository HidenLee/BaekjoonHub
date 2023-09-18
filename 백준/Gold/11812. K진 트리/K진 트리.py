# https://www.acmicpc.net/problem/11812

# def sol1(K,x,y):
#     def findparent(a,k):
#         temp = a % k
#         if temp <= 1: # 1, 0
#             return a // k
#         else:
#             return (a + (k-temp)) // k
        
#     xparents = [x]
#     yparents = [y]
#     while xparents[-1] != 1:
#         xparents.append(findparent(xparents[-1],K))
#     while yparents[-1] != 1:
#         temp = findparent(yparents[-1],K)
#         if temp in xparents:
#             return(xparents.index(temp)+len(yparents))
#         yparents.append(temp)
#     if y == 1:
#         return(len(xparents)-1)


def sol2(K,x,y):
    def findparent2(a,k):
        return (a+k-2)//k
    ans = 0
    while True:
        if x == y:
            return ans
        if x > y:
            x = findparent2(x,K)
        else:
            y = findparent2(y,K)
        ans += 1


N, K, Q = map(int,input().split())
for _ in range(Q):
    x, y = map(int,input().split())

    if K > 1:
        # sol1(K,x,y)
        print(sol2(K,x,y))
    else:
        print(abs(x-y))