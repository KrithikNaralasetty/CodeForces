#1136A in codeforces
n = int(input())
chapters = []
for _ in range(n):
	chapters.append(list(map(int,input().split())))
k = int(input())
i = 0
while i < n:
	if k<=chapters[i][1]:
		break
	else:
		i+=1
print(n-i)