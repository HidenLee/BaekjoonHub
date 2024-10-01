# https://www.acmicpc.net/problem/1043

# union find
N ,M = map(int,input().split())

parents = list(range(N+1))
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parents[rootY] = rootX


trueIpt = list(map(int,input().split()))

if trueIpt[0] == 0:
    print(M)
    exit()

true = trueIpt[1:]

parties = []
for _ in range(M):
    ipt = list(map(int,input().split()))
    party = ipt[1:]
    for idx in range(1,len(party)):
        union(party[0],party[idx])
    parties.append(party)

for true_man in true:
    union(true[0],true_man)

count = 0
for party in parties:
    if all(find(person) != find(true[0]) for person in party):
        count += 1
print(count)