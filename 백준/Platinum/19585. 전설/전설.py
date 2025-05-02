C, N = map(int, input().split())
color = {}
team = {}
for i in range(C):
    now = color
    for alp in input():
        if alp not in now:
            now[alp] = {}
        now = now[alp]
    now["end"] = True

team = set(input() for _ in range(N))

for i in range(int(input())):
    ipt = input()
    now = color
    for idx, alp in enumerate(ipt):
        if "end" in now and ipt[idx:] in team: 
            print("Yes")
            break
        if alp not in now:
            print("No")
            break
        now = now[alp]
    else:
        print("No")