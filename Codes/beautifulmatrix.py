#263A in codeforces
matrix = []
for _ in range(5):
	matrix.append(list(map(int,input().split())))
for i in range(5):
	flag = 0
	for j in range(5):
		if matrix[i][j] == 1:
			flag=1
			break
	if flag == 1:
		break
moves = abs(2-i)+abs(2-j)
print(moves)