A, B = map(int,input().split())

import math
prime = [True for i in range(B+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
dp = [0 for _ in range(B+1)]
# 에라토스테네스의 체
for i in range(2, int(math.sqrt(B)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if prime[i]: # i가 소수인 경우(남은 수인 경우)
        # dp[i] = 1
        for j in range(i * i, B + 1, i):  # Start from i*i and increment by i
            prime[j] = False

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함


# Calculating the number of prime factors for each number using dynamic programming
for i in range(2, B + 1):
    if dp[i] == 0:  # If the prime factor count hasn't been set yet
        # Start from i and increment in steps of i, marking all multiples
        for j in range(i, B + 1, i):
            dp[j] = dp[j // i] + 1  # Set dp[j] = dp[j // i] + 1

ans = 0
prime[0] = False
prime[1] = False
for i in range(A,B+1):
    if prime[dp[i]]:
        ans += 1
# print(dp)
# print(prime)
print(ans)
