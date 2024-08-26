arr = list(map(int,input().split()))

def gcd(num1,num2):
    r = num1 % num2
    b = min(num1,num2)
    a = max(num1,num2)
    while b:
        r = a % b
        a = b
        b = r
    return a

def lcm(num1,num2):
    return num1*num2 //gcd(num1,num2)

ans = 1000000
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans = min(ans,lcm(arr[i],lcm(arr[j],arr[k])))
print(ans)
# abcde
# abc abd abe
# acd ace 
# ade
# bcd bce
# bde
# cde 
