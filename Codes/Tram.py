#116A in codeforces
n = int(input())
x,z = 0,0
for _ in range(n):
	a,b = map(int,input().split())
	z += b-a
	if x<z:
		x = z
print(x)