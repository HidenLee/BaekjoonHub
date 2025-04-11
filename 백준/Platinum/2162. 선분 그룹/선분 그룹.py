def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[b] = a


def CCW(a,b,c):
    ca = (a[0]-c[0],a[1]-c[1])
    cb = (b[0]-c[0],b[1]-c[1])
    delta = ca[0]*cb[1] - ca[1]*cb[0]
    if delta > 0 :
        return 1
    elif delta == 0 : 
        return 0
    else:
        return -1

def intersection(l1,l2):
    p1,p2 = ((l1[0],l1[1]),(l1[2],l1[3]))
    q1,q2 = ((l2[0],l2[1]),(l2[2],l2[3]))
    flag1 = CCW(p1,p2,q1) * CCW(p1,p2,q2)
    flag2 = CCW(q1,q2,p1) * CCW(q1,q2,p2)

    # case of two line have same ccw product, we should check inline or far-away
    if flag1 == 0 and flag2 == 0:
        if (max(p1,p2) >= min(q1,q2) and min(p1,p2) <= max(q1,q2)) or (max(q1,q2) >= min(p1,p2) and min(q1,q2) <= max(p1,p2)):
            return True
        return False

    # if they have diffent ccw product, it is intersection case when ccw are have oposite return
    return flag1 <= 0 and flag2 <= 0

N = int(input())
parent = list(range(N))
table = [tuple(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if intersection(table[i],table[j]):
            union(i,j)
maxCount = 1
visit = dict()
for elm in parent:
    elm = find(elm)
    if not elm in visit:
        visit[elm] = 1
    else:
        visit[elm] += 1
        if maxCount < visit[elm]:
            maxCount = visit[elm]
print(len(visit.keys()))
print(maxCount)