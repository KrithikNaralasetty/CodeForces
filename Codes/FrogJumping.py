#1077A in codeforces
for _ in range(int(input())):
	a,b,k = map(int,input().split())
	right = k - k//2
	left = k//2
	frog = (right*a) - (left*b)
	print(frog)