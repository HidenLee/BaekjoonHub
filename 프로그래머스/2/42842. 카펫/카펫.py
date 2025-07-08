def solution(brown, yellow):
    # 2w+2h -4 = B
    # (w-2)*(h-2) = Y
    # w+h = (B+4)/2
    # w*h = Y+B
    for x,y in [((brown+yellow)//a,a) for a in range(1,int((brown+yellow)**0.5)+1) if not (brown+yellow)%a ]:
        if x + y == (brown + 4) // 2:
            return [x,y]