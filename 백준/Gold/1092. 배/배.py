N = int(input())
cranes = sorted(list(map(int,input().split())),reverse=True)
M = int(input())
boxes = sorted(list(map(int,input().split())))

if boxes[-1] > cranes[0]:
    print(-1)
    exit()

cnt = 0
while boxes:
    for crane in cranes:
        for i in range(len(boxes)-1,-1,-1):
            if boxes[i] <= crane:
                boxes = boxes[:i] + boxes[i+1:]
                break
    cnt+= 1
print(cnt)