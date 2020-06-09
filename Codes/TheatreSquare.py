#1A in codeforces
n,m,a = map(int,input().split())
r,c = n//a , m//a
if n%a>0:
	r = r+1
if m%a>0:
	c=c+1
print(r*c)