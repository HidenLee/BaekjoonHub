N = int(input())
table = list(map(int, input().split()))
for i in range(3):
    table[i] = [table[i],table[i]]
for tc in range(1,N):
    temp =  list(map(int, input().split()))
    origin = [x for x in table]
    table[0] = [temp[0] + max(origin[0][0],origin[1][0]), temp[0] + min(origin[0][1],origin[1][1])]  
    table[1] = [temp[1] + max(origin[0][0],origin[1][0],origin[2][0]), temp[1] + min(origin[0][1],origin[1][1],origin[2][1])]  
    table[2] = [temp[2] + max(origin[1][0],origin[2][0]), temp[2] + min(origin[1][1],origin[2][1])]  
print(max([table[x][0] for x in range(3)]),min([table[y][1] for y in range(3)]))