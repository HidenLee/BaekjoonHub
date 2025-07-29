def solution(h1, m1, s1, h2, m2, s2):
    def count(time):
        answer = -1
        
        hRad = (time % 43200) / 43200 * 360
        mRad = (time % 3600) / 3600 * 360
        sRad = (time % 60) / 60 * 360
        if sRad >= mRad:
            answer += 1
        if sRad >= hRad:
            answer += 1
        answer += (time // 60)*2 - time//3600
        if time >= 43200:
            answer -= 2 
        return answer
    time1 = h1*3600 + m1*60 + s1
    time2 = h2*3600 + m2*60 + s2
    return count(time2) - count(time1) + (1 if time1 in [0,43200] else 0)
