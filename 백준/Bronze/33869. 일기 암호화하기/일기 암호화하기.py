key = {chr(i): False for i in range(65, 91)}
visit = set()
idx = 65
for elm in input():
    if elm in visit:
        continue
    while idx <= 90 and not key[chr(idx)]:
        key[chr(idx)] = elm
        visit.add(elm)  
        idx += 1
        break
jdx = 65
for kdx in range(idx, 91):
    while jdx <= 90 and chr(jdx) in visit:
        jdx += 1
    if not key[chr(kdx)]:
        key[chr(kdx)] = chr(jdx)
        jdx += 1
print("".join(key[char] for char in input()))    