#1270A in codeforces
t = int(input())
for _ in range(t):
	n,k1,k2 = map(int,input().split())
	player_1 = list(map(int,input().split()))
	player_2 = list(map(int,input().split()))
	a = max(player_1)
	b = max(player_2)
	while player_1 and player_2:
		try:
			a = max(player_1)
		except:
			a = 0
		try:
			b = max(player_2)
		except:
			b = 0
		if a<b:
			player_1.remove(a)
			player_2.append(a)
		elif a>b:
			player_1.append(b)
			player_2.remove(b)
	if not player_2:
		print("YES")
	elif not player_1:
		print("NO")