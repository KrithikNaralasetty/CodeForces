#615A in codeforces
n,m = map(int,input().split())
a = []
for _ in range(n):
	bulbs = list(map(int,input().split()))
	bulbs = set(bulbs[1:])
	for i in bulbs:
		if i not in a:
			a.append(i)
if len(a) == m:
	print("YES")
else:
	print("NO")