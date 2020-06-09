#855A in codeforces
n = int(input())
names = {}
for _ in range(n):
	z = input()
	if z not in names.keys():
		names[z]=1
		print("NO")
	else:
		names[z]+=1
		print("YES")