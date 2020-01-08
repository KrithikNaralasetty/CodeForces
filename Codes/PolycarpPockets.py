#1003A in codeforces
n = int(input())
pockets = 0
coins = list(map(int,input().split()))
distinct = set(coins)
if len(coins)>len(distinct):
	if min(coins) == max(coins):
		pockets=n
	else:
		while len(coins)!=0:
			for i in distinct:
				coins.remove(i)
			distinct = set(coins)
			pockets+=1
elif len(coins) == len(distinct):
	pockets = 1
print(pockets)