#703A in codeforces
n = int(input())
games_won = 0
for _ in range(n):
	a,b = map(int,input().split())
	if a>b:
		games_won+=1
	elif a<b:
		games_won-=1
if games_won>0:
	print("Mishka")
elif games_won<0:
	print("Chris")
else:
	print("Friendship is magic!^^")