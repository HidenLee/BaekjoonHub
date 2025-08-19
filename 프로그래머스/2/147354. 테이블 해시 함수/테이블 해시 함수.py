def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    answer = sum([i%row_begin for i in data[row_begin-1]])
    for r in range(row_begin,row_end):
        answer ^= sum([i%(r+1) for i in data[r]])
    return answer