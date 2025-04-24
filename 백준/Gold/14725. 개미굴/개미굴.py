dic = {}
for line in [list(input().split())  for _ in range(int(input()))]:
    now = dic
    for word in line[1:]:
        if word not in now:
            now[word] = {}
        now = now[word]

def pprint(node, depth):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        pprint(node[key], depth + 1)
pprint(dic, 0)