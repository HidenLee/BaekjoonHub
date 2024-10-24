N = int(input())
table = [[True if x == "Y" else False for x in list(input())] for _ in range(N)]
print(max([sum([1 if A != B and (table[A][B] or any([table[B][C] for C in [i for i,flag in enumerate(table[A]) if flag and i != B and i !=A]]) ) else 0 for B in range(N)]) for A in range(N)]))

