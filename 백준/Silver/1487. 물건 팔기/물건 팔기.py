N = int(input())
table = sorted([tuple(map(int,input().split())) for _ in range(N)], key=lambda x: (x[0],x[1]))
answer = 100001
maxValue = 0
for i in range(N):
    price, tax = table[i]
    value = price - tax
    for j in range(i+1,N):
        if table[j][1] > price:
            continue
        value += (price - table[j][1])
    # print(price,value)
    if maxValue < value:
        answer = price
        maxValue = value
    elif maxValue == value:
        answer = min(answer,price)
print(answer if maxValue else 0)