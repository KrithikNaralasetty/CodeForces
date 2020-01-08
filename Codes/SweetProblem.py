#1263A in codeforces
q = int(input())
for _ in range(q):
	candies = 0
	r,g,b =  list(map(int,input().split()))
	z = min (r,g,b)
	candies+= z
	if z>r and z<=min(g,b):
		g = g-z
		b = b-z
	elif z>g and z<=min(r,b):
		r = r-z
		b = b-z
	elif z>b and z<=min(r,g):
		r = r-z
		g = g-z