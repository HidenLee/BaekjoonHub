def solution(n, k):
    import math
    prime = set()
    def isPrime(n):
        if n == "" or n == "1":
            return False
        n = int(n)
        if n in prime:
            return True
        for i in range(2,int(math.sqrt(n)+1)):
            if not n % i:
                return False
        prime.add(n)
        return True
    zeros = []
    def trans(n,k):
        base = ""
        while n > 0:
            n, mod = divmod(n,k)
            base += str(mod)
        return base[::-1]      
    t = trans(n,k)
    print(t.split("0"))
    return sum([1 if isPrime(sub) else 0 for sub in t.split("0")])
