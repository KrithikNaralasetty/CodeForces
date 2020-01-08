#758A in codeforces
n = int(input())
welfares = list(map(int,input().split()))
welfares.sort()
cost = welfares[-1]
money = 0
for i in welfares:
	money+=cost-i
print(money)