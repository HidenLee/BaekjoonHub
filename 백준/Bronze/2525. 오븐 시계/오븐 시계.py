H, M = map(int,input().split())
M += int(input())
while M >= 60:
    M -= 60
    H += 1
while H >= 24:
    H -= 24
print(H,M)