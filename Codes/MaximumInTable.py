#509A in codeforces
n = int(input())
matrix = [] 
matrix.append(list(1 for i in range(n)))
z = [1]
for i in range(1,n):
	z.append(0)
for i in range(1,n):
	matrix.append(z)
for i in range(1,n):
	for j in range(1,n):
		matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
print(matrix[-1][-1])