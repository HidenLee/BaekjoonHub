_ = input()
ari = [1 for x in range(1001)]
ari[1] = 0
for i in range(2,1001):
    if ari[i] == 0:
        continue
    j = 2
    while i*j < 1001:
        ari[i*j] = 0
        j += 1
    
        
print(sum([ari[x] for x in map(int,input().split())]))