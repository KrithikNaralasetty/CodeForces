#177A1 in codeforces
n = int(input())
matrix = []
for _ in range(n):
	matrix.append(list(map(int,input().split())))
elements_sum = 0
#sum of middle row
elements_sum+=sum(matrix[n//2])
#sum of middle column
for i in range(n):
	elements_sum+=matrix[i][n//2]
#sum of first diagonal
for i in range(n):
	elements_sum+=matrix[i][i]
#sum of second diagonal
for i in range(n):
	elements_sum+=matrix[n-i-1][i]
print(elements_sum-(3*matrix[n//2][n//2]))