#1285B in codeforces
t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	flag = 0
	yasser = sum(a)
	i,j = 0,0
	while i < n:
		if a[i] <0:
			adel = sum(a[j:i])
			print(a[j:i])
			if adel >= yasser:
				flag = 1

			i = i+1
			j = i
			continue
		else:
			i = i+1
	if flag == 0:
		print("YES")
	else:
		print("NO")