_ = input()
cards = set(list(input().split()))
__ = input()
print(*[1 if x in cards else 0 for x in input().split()])
