from collections import deque

def read_n(n):
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    return a

def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, M, K, A, B = map(int, input().split())
        A_time = read_n(N)
        B_time = read_n(M)
        arrivals = read_n(K)

        arr_list = sorted((arrivals[i], i+1) for i in range(K))
        arr_idx = 0

        reception = [(0, 0) for _ in range(N)]
        repair = [(0, 0) for _ in range(M)]

        reception_wait = deque()
        repair_wait = deque()

        record = [[0, 0] for _ in range(K+1)]

        done = 0
        time = 0

        while done < K:
            while arr_idx < K and arr_list[arr_idx][0] == time:
                reception_wait.append(arr_list[arr_idx][1])
                arr_idx += 1

            for i in range(N):
                cust, endt = reception[i]
                if cust and endt == time:
                    repair_wait.append(cust)
                    reception[i] = (0, 0)

            for j in range(M):
                cust, endt = repair[j]
                if cust and endt == time:
                    repair[j] = (0, 0)
                    done += 1

            for i in range(N):
                cust, _ = reception[i]
                if not cust and reception_wait:
                    c = reception_wait.popleft()
                    reception[i] = (c, time + A_time[i])
                    record[c][0] = i + 1

            for j in range(M):
                cust, _ = repair[j]
                if not cust and repair_wait:
                    c = repair_wait.popleft()
                    repair[j] = (c, time + B_time[j])
                    record[c][1] = j + 1

            time += 1

        ans = sum(c for c in range(1, K+1) if record[c][0] == A and record[c][1] == B)
        if ans == 0:
            ans = -1
        print(f"#{tc} {ans}")

if __name__ == "__main__":
    solve()
