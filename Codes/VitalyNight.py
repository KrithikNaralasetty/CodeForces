#595A in codeforces
n,m = map(int,input().split())
awake = 0
for _ in range(n):
	windows = list(map(int,input().split()))
	for i in range(0,2*m,2):
		win = windows[i:i+2]
		if 1 in win:
			awake+=1
print(awake)