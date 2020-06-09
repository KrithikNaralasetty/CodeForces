# 546A in codeforces
k,n,w = map(int,input().split())
cost = 0
for _ in range(1,w+1):
	cost += _*k
if cost<=n:
	print(0)
else:
	print(cost-n)