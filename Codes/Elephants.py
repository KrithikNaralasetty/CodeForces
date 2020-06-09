#617A in codeforces
x = int(input())
i = 5
steps = 0
while x>0:
	if x>=i:
		z = x//i
		steps+=z
		x-=(z*i)
	i-=1
print(steps)