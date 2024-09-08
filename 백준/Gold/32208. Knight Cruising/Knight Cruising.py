# from itertools import permutations
# comb = permutations([1,-1,0],3)
# table = set([])
# for i,j,k in list(comb):
#     table.update([(i*a,j*b,k*c) for a in [-1,1] for b in [-1,1] for c in [-1,1]])
# table.add((0,0,0))
# print(table)

# def sol1(ipt):
#     x, y, z = ipt
#     if ((nx := x % 3) == 2): nx = -1
#     if ((ny := y % 3) == 2): ny = -1
#     if ((nz := z % 3) == 2): nz = -1
#     return (nx,ny,nz) in table

# def sol2(ipt):
#     x, y, z = ipt
#     # Check if (x + y + z) is even
#     if (x + y + z) % 2 != 0:
#         return False
#     # Check if x ≡ (y + z) (mod 4)
#     if x % 4 != (y + z) % 4:
#         return False
#     return True

# def sol3(ipt):
#     x , y, z = ipt
#     if (x+y+z)%2:
#         return False
#     return True

# N = int(input())
# for _ in range(N):
#     if sol3(map(int,input().split())):
#         print("YES")
#     else:
#         print("NO")

import sys
ipt = sys.stdin.read().splitlines()
N = int(ipt[0])

def sol3(ipt):
    x , y, z = ipt
    if (x+y+z)%2:
        return False
    return True

results = []

for i in range(1,N+1):
    x, y, z = map(int, ipt[i].split())
    if sol3((x, y, z)):
        results.append("YES")
    else:
        results.append("NO")
sys.stdout.write("\n".join(results) + "\n")