#1311 A in codeforces
t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	if a>b:
		if (a-b)%2 == 0:
			print("1")
		else:
			print("2")
	elif a == b:
		print("0")
	else:
		if (b-a)%2 == 0:
			print("2")
		else:
			print("1")