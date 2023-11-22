# https://www.acmicpc.net/problem/30677

N, K, C, R = map(int,input().split())
base = list(map(int, input().split()))
s = list(map(int, input().split()))
p = list(map(int, input().split()))
skill = [0 for _ in range(K)]
stardust = 0
combo = 0
exhaust = 0
for _ in range(N):
    i = int(input())

    if exhaust > 100:
        stardust = -1
        break
    
    if(i == 0):
        exhaust = max(0,exhaust-R)
        combo = 0
        continue
    # print(base[i-1]*(1+ combo*C/100)*(1+s[i-1]*skill[i-1]/100),int(base[i-1]*(1+ combo*C/100)*(1+s[i-1]*skill[i-1]/100)))
    stardust += int((base[i-1]) * (100+ combo*C) * (100+s[i-1]*skill[i-1])/10000) 
    skill[i-1] += 1
    combo += 1
    exhaust += p[i-1]
    
    if exhaust > 100:
        stardust = -1
        break
    

print(stardust)