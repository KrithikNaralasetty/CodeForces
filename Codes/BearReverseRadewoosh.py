#658A in codeforces
n,c = map(int,input().split())
scores = list(map(int,input().split()))
times = list(map(int,input().split()))
score_1, score_2 = 0,0
x = 0
for i in range(0,n):
	x += times[i]
	score_1+=max(0,scores[i] - x*c)
x = 0
for i in range(n-1,-1,-1):
	x += times[i]
	score_2+=max(0,scores[i] - x*c)
if score_1>score_2:
	print("Limak")
elif score_1 == score_2:
	print("Tie")
else:
	print("Radewoosh")