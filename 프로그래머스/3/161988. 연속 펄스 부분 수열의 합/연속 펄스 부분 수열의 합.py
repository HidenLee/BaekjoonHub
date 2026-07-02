def solution(sequence):
    ans = -1 * 10e6 * 5 * 10e6

    cur1 = cur2 = 0

    for idx, x in enumerate(sequence):
        a = x if idx % 2 == 0 else -x
        b = -a

        cur1 = max(a, cur1 + a)
        cur2 = max(b, cur2 + b)

        ans = max(ans, cur1, cur2)

    return ans