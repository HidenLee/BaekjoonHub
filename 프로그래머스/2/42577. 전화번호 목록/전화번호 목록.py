def solution(phone_book):
    trie = {}
    for elm in phone_book:
        now = trie
        for num in elm:
            if "*" in now:
                return False
            if num in now:
                now = now[num]
                continue
            now[num] = {}
            now = now[num]
        if now.keys():
            return False
        now["*"] = True
    return True