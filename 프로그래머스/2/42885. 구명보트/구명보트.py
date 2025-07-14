def solution(people, limit):
    people.sort()
    N = len(people)
    left = 0
    answer = 0
    for idx in range(N):
        right = N - 1 - idx
        if left > right:
            break
        if people[left] + people[right] <= limit:
            left += 1
        answer += 1

    return answer