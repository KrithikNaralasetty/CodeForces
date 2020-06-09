#897A in codeforces
n,m = map(int,input().split())
string = list(i for i in input())
for _ in range(m):
	l,r,c1,c2 = map(str,input().split())
	l = int(l)-1
	r = int(r)
	for i in range(l,r):
		if string[i] == c1:
			string[i] = c2
for i in string:
	print(i,end="")