# https://www.acmicpc.net/problem/2749
n = int(input())
piv = [0,1]
target = n % 1500000
for i in range(2,target+1):
    piv.append((piv[i-1]+piv[i-2])%1000000)
print(piv[target])