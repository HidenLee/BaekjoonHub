def insert(word):
    now = trie
    for alp in word:
        if alp not in now.keys():
            now[alp] = {}
        now = now[alp]
    now['end'] = True

def search(word):
    now = trie
    cnt = 1
    for idx in range(1,len(word)):
        now = now[word[idx-1]]
        if len(now.keys()) > 1 or 'end' in now:
            cnt += 1
    return cnt



try:
    while True:
        dic = [input() for _ in range(int(input()))]
        trie = {}
        for word in dic:
            insert(word)
        ans = [search(word) for word in dic]
        print(f"{round(sum(ans)/len(ans),2):.2f}")
                    

except:
    exit()
