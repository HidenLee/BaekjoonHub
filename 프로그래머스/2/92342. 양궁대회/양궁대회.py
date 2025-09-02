def solution(n, info):
    best = None
    best_diff = -1  # score difference (Lion - Apeach)

    # iterate all subsets of scores Lion tries to win
    for mask in range(1 << 11):
        used = 0
        shot = [0]*11

        # try to win each selected score k
        ok = True
        for k in range(11):
            if mask & (1 << k):
                need = info[k] + 1
                used += need
                if used > n:  # over budget
                    ok = False
                    break
                shot[k] = need

        if not ok:
            continue

        # compute score diff
        lion = 0
        apeach = 0
        for k in range(11):
            score = 10 - k
            if shot[k] > 0:          # Lion wins this ring
                lion += score
            elif info[k] > 0:        # Apeach gets it if she shot here
                apeach += score
        diff = lion - apeach

        # put all remaining arrows into 0-point ring (index 10)
        if used < n:
            shot[10] += (n - used)

        # keep best by diff, then tie-break
        if diff > best_diff:
            best_diff = diff
            best = shot
        elif diff == best_diff and best is not None:
            # prefer more arrows in lower scores: compare from idx 10 down to 0
            for i in range(10, -1, -1):
                if shot[i] > best[i]:
                    best = shot
                    break
                elif shot[i] < best[i]:
                    break

    return best if best is not None and best_diff > 0 else [-1]

def solution1(n, info):
    answer = [0 for _ in range(11)]
    max_grade = 1
    for bit in range(1 << 11):
        grade = 0
        count = 0
        case = [0 for _ in range(11)]
        for k in range(11):
            if bit & (1<<k) and count < n - info[k]:
                count += info[k] + 1
                grade += 10 - k
                case[k] = info[k] + 1
            elif info[k]:
                grade -= 10 - k
        if max_grade < grade:
            max_grade = grade
            answer = case
        elif max_grade == grade:
            if any([answer[idx] < case[idx] for idx in range(10,-1,-1)]):
                answer = case
        for jdx in range(10,-1,-1):
            if count == n:
                break
            case[jdx] += min(n-count,info[jdx])
            count += case[jdx]
            
    return answer if sum(answer) else [-1]