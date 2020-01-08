#1223A in codeforces
output=[]
for _ in range(int(input())):
	sticks = 0
	n = int(input())
	if n%2 == 0:
		if n == 2:
			sticks = 2
	else:
		sticks = 1
	output.append(sticks)
for i in output:
	print(i)