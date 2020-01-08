#510A in code forces
#Wrong Code

n,m=map(int,input().split())
matrix = list(list("." for i in range(m)) for j in range(n))
for i in range(0,m):
	matrix[0][i]="#"
for i in range(1,n):
	j = i+1
	if j%2 == 0:
		if j%4==0:
			matrix[i][0]="#"
		else:
			matrix[i][m-1]="#"
	else:
		for j in range(0,m):
			matrix[i][j]="#"
for i in matrix:
	for j in i:
		print(j,end="")
	print("")