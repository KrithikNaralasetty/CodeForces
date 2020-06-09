#1097A in codeforces
base = list(char for char in input())
cards = list(map(str,input().split()))
flag = 0
for _ in cards:
	if base[0] in _ or base[1] in _:
		flag = 1
		break
if flag == 1:
	print("YES")
else:
	print("NO")