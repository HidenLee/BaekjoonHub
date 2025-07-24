def solution(diffs, times, limit):
    high = max(diffs)
    low = 1
    while low < high:
        mid = (high+low) // 2
        count = times[0]
        if diffs[0] > mid:
            count *= (diffs[0]-mid+1)
        for i in range(1,len(diffs)):
            count += times[i] if diffs[i] <= mid else times[i] + (times[i]+times[i-1])*(diffs[i]-mid)
            if count > limit:
                break
        if count <= limit:
            high = mid
            continue
        low = mid + 1
    return low