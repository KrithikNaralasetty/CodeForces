#984A in codeforces
n = int(input())
board = list(map(int,input().split()))
for i in range(n-1):
	if i%2 == 0:
		x = max(board)
		board.remove(x)
	else:
		x = min(board)
		board.remove(x)
print(board[0])