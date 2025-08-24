def solution(arrayA, arrayB):
    def gcd(a,b):
        if b == 0 : 
            return a
        return gcd(b, a%b)
    gca = arrayA[0]
    gcb = arrayB[0]
    for _ in range(len(arrayA)):
        gca = gcd(gca,arrayA[_])
        gcb = gcd(gcb,arrayB[_])
    answer = 0
    for _ in range(len(arrayA)):
        if not arrayA[_] % gcb:
            break
    else:
        answer = max(answer,gcb)
    
    for _ in range(len(arrayB)):
        if not arrayB[_] % gca:
            break
    else:
        answer = max(answer,gca)

            
    return answer