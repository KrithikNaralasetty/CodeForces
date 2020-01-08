#1064A in codeforces
a,b,c = map(int,input().split())
z = max(a,b,c)
s = a+b+c - z
if z<s:
	print(0)
elif z>=s:
	if z == a:
		x = b+c
	elif z == b:
		x = a+c
	else:
		x = a+b
	inc = z - x
	print(inc+1)