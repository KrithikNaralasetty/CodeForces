#1316A in codeforces
t = int(input())
for _ in range(t):
	n,m = map(int,input().split())
	grades = list(map(int,input().split()))
	total = sum(grades)
	if total<m:
		print(total)
	else:
		print(m)