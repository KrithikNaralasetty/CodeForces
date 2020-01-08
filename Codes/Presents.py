#136A in codeforces
n = int(input())
x = list(map(int,input().split()))
a={}
e=0
for i in range(0,n):
	a[x[i]] = i+1
for i in range(1,n+1):
	print(a[i],end=" ")