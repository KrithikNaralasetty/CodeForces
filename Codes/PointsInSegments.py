#1015A in codeforces
n,m = map(int,input().split())
points = list(i for i in range(1,m+1))
for _ in range(n):
	l,r = map(int,input().split())
	for i in range(l,r+1):
		if i in points:
			points.remove(i)
print(len(points))
for i in points:
	print(i,end=" ")