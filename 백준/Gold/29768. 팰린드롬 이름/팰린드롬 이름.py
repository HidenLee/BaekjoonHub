N, K = map(int, input().split())
print('a'*(N-K) + ''.join([chr(ord('a') + i) for i in range(K)]))
