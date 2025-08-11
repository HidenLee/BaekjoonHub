algs = {}
for _ in range(int(input())):
    alg, alg_lev = input().split()
    alg_lev = int(alg_lev)
    algs[alg] = alg_lev

member = {}
for _ in range(int(input())):
    name, lev = tuple(input().split())
    member[name] = int(lev)

name = ""
for _ in range(int(input())):
    ipt = list(input().split())
    if ipt[-1][-1] == "!":
        name = ipt[0]
        print("hai!")
        continue
    
    level = member[name]
    algo1 = algo2 = ""
    
    gap = 31
    for alg,diff in algs.items():
        value = abs(level - diff)
        if value < gap:
            gap = value
            algo1 = alg
        elif value == gap:
            algo1 = min(algo1, alg)
    gap = 31
    for alg,diff in algs.items():
        if alg == algo1:
            continue
        value = abs(level - diff)
        if value < gap:
            gap = value
            algo2 = alg    
        elif value == gap:
                    algo2 = min(algo2, alg)
    print(algo2+" yori mo "+algo1)
