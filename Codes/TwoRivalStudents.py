#1257a in codeforces
t = int(input())
for _ in range(t):
	n,x,a,b = map(int,input().split())
	pos = abs(a-b)
	if pos == n-1:
		print(n-1)
	elif pos<n-1:
		pos+=x
		if pos>n-1:
			pos = n-1
		print(pos)