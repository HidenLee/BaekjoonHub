comb = [[0]*53 for _ in range(53)]
for i in range(53):
    comb[i][0] = 1
for i in range(1,53):
    for j in range(1,53):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j])

def solve(n):
    ans = 0
    flag = 1
    for i in range(1,n//4+1):
        ans += comb[52-4*i][n-4*i] * comb[13][i] * flag
        ans %= 10007
        flag *= -1
    return ans
print(solve(int(input())))


#(13)C(i) * (52-4i)C(n-4i)