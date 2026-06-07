def solution(files):
    def sortkey(elm):
        for idx, alp in enumerate(elm):
            if alp.isdecimal():
                left = idx
                while idx < len(elm) and elm[idx].isdecimal():
                    idx += 1
                return (elm[:left].lower(), int(elm[left:idx]))
    
    return sorted(files, key=lambda x:sortkey(x))