def solution(n, infection, edges, k): 
    # a->b와 b->a 순서의 결과가 다르므로 모든 경우의수 탐색 필요
    # k의 최댓값은 10, type은 A,B,C 3가지 고정
    # 연산 최대 횟수 : 3C1 + 3C2 + 3C3 + ... + 3C10  = (3+1)**10 > 10**6

    route = {1:[],2:[],3:[]}
    for x,y,z in edges:
        route[z].append((x,y))
        route[z].append((y,x))

    def calc(typ,data): # typ에따라 route를 참고해 data 변조
        flag = True
        while flag: # 변경점 없으면 루프 중단  
            flag = False
            for fr,to in route[typ]:
                while data & (1<<fr) and not data &(1<<to): # fr이 감염되고 to가 감염되지 않은 경우
                    data |= 1 << to # to를 감염시킨다
                    flag = True
        return data
    initial = 1 << infection         
    answer = initial.bit_count()
        
    stack = [(1,initial),(2,initial),(3,initial)] # (열었던 파이프기록,배양체 상태 2진 표현)
    while stack and answer < n:
        case, cells = stack.pop()
        cells = calc(case%10,cells) 
        if case >= 10**(k-1):
            answer = max(answer,cells.bit_count())
            # print(case,bin(cells))
            continue
        c = case % 10
        for nxt in [x for x in [1,2,3] if x!= c]:
            stack.append((case*10 + nxt,cells))
    
    return answer
