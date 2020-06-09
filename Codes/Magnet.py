#344A in codeforces
n = int(input())
groups = 1
z = int(input())
for _ in range(n-1):
	x = int(input())
	if x != z:
		z = x
		groups+=1
print(groups)