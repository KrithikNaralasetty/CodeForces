n = int(input())
problems_solved = 0
for _ in range(n):
	a,b,c = map(int,input().split())
	z = a+b+c
	if z>=2:
		problems_solved+=1
print(problems_solved)