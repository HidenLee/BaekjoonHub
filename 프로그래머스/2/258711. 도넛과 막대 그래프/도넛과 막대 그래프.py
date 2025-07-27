def solution(edges):
    from collections import deque
    answer = [0,0,0,0]
    routes = {}
    alist = set([])
    blist = set([])
    for index in range(len(edges)):
        a, b = edges[index][0], edges[index][1]
        alist.add(a)
        blist.add(b)
        if a in routes:
            routes[a].append(b)
        else:
            routes[a] = [b]
    
    # 들어오는 간선이 없다면 그 녀석이 outlier
    # outlier와 연결된 노드들이 각 그래프의 representer
    # representer마다 그래프를 유추해 answer 배열에 합산
    for elm in alist:
        if elm not in blist:
            if len(routes[elm]) < 2:
                continue
            answer[0] = elm
            while routes[elm]:
                lines = 0
                representer = routes[elm].pop()
                deq = deque([representer])
                visit = set()
                visit.add(representer)
                while deq:
                    now = deq.popleft()
                    if not now in routes:
                        continue
                    for nxt in routes[now]:
                        lines += 1
                        if not nxt in visit:
                            visit.add(nxt)
                            deq.append(nxt)
                nodes = len(visit)
                if nodes == lines:
                    answer[1] += 1
                elif nodes > lines:
                    answer[2] += 1
                else:
                    answer[3] += 1
            return answer                    
