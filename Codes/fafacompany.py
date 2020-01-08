#935A in codeforces
n = int(input())
ways = 0
for i in range(1,(n//2)+1):
	n1 = n-i
	if n1%i == 0:
		ways +=1
print(ways)