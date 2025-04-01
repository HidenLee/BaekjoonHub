while(True):
    sq = [x**2 for x in map(int,input().split())]
    if not any(sq) :
        break
    if sum(sq) // 2 in sq:
        print("right")
        continue
    print("wrong")