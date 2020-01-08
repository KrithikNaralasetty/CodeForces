#732A in codeforces
k,r = map(int,input().split())
z = k-r
if z%10 == 0 or k%10 == 0:
	print(1)
else:
	for i in range(2,11):
		z = k*i
		if (z-r)%10 == 0 or z%10 ==0:
			print(i)
			break