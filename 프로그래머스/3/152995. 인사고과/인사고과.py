def solution1(scores): # 딕셔너리 순회 O(N**2) -> 시간초과
    근태별_제일높은동평 = {} # 근태점수별 가장 높은 동평점수
    동평별_제일높은근태 = {} # 동평점수별 가장 높은 근태점수
    answer = 1
    철수_근태, 철수_동평 = scores[0]
    for 근태,동평 in sorted(scores,key=lambda x: (-x[0], x[1])):
        if any([근태별_제일높은동평[x] > 동평 for x in 근태별_제일높은동평.keys() if x > 근태]) : continue
        
        if 근태+동평 > 철수_근태 + 철수_동평:
            if 근태 > 철수_근태 and 동평 > 철수_동평:
                return -1
            answer += 1
        
        근태별_제일높은동평[근태] = max(동평,근태별_제일높은동평.get(근태,0))
        동평별_제일높은근태[동평] = max(근태,동평별_제일높은근태.get(동평,0))
        
    return answer
    

def solution(scores):
    철수 = scores[0]
    가장_큰_동평 = 0
    answer = 1
    for 근태, 동평 in sorted(scores[1:],key=lambda x: (-x[0],x[1])):
        if 근태 > 철수[0] and 동평 > 철수[1]:
            return -1
        if 동평 < 가장_큰_동평:
            continue
        가장_큰_동평 = 동평
        answer += 1 if 근태+동평>sum(철수) else 0
    return answer