#1017A in codeforces
n = int(input())
thomas  = sum(list(map(int,input().split())))
rank = 1
for _ in range(n-1):
	marks = sum(list(map(int,input().split())))
	if marks>thomas:
		rank+=1
print(rank)