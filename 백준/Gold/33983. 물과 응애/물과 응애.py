cntH = 0
cntO = 0
N = int(input())
ipt = list(input())

left = right = 0
for i in range(N):
    if ipt[i] == 'H':
        cntH += 1
        left += 1
    elif ipt[i] =='O':
        cntO += 1
        if left < 1 :
            print('mix')
            exit()
        left -= 1
    if ipt[-1-i] == 'H':
        right += 1
    elif ipt[-1-i] == 'O':
        if right < 1 :
            print('mix')
            exit() 
        right -= 1  
else:
    print('pure' if cntH == cntO * 2 else 'mix')
