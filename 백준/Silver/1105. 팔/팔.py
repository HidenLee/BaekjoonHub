L, R = input().split()

if len(L) == len(R):
    eights = 0
    for idx in range(len(L)):
        if L[idx] != R[idx]:
            # if L[idx] == "8" and R[idx] == "9":
            #     eights += 1   
            break
        elif L[idx] == "8":
            eights += 1
    print(eights)
else:
    print(0)