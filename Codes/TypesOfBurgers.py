#1207A in codeforces
q = int(input())
for _ in range(q):
	cost = 0
	b,p,f = map(int,input().split())
	h,c = map(int,input().split())
	b = b//2
	if h>c:
		z = min(b,p)
		cost = z*h
		if z<b:
			b-=z
			z =  min(b,f)
			cost+=z*c
	elif h == c:
		z = min(b,p+f)
		cost = z*h
	elif h<c:
		z = min(b,f)
		cost = z*c
		if z<b:
			b-=z
			z =  min(b,p)
			cost+=z*h
	print(cost)