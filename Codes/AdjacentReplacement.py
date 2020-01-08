#1006A in codeforces
n = int(input())
numbers = list(map(int,input().split()))
for i in range(n):
	if numbers[i]%2==0:
		numbers[i]-=1
for i in numbers:
	print(i,end = " ")