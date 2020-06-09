#228A in codeforces
colors = set(map(int,input().split()))
if len(colors)<4:
	print(4-len(colors))
else:
	print(0)