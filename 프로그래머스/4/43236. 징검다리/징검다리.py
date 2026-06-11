def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        removed = 0
        prev = 0

        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock

        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer