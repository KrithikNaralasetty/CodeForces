#1167A in codeforces
q = int(input())
for _ in range(q):
	n = int(input())
	number = input()
	if n<11:
		print("NO")
	elif n== 1:
		if number[0]=="8":
			print("YES")
		else:
			print("NO")
	else:
		n = n-11
		sub = number[:n+1]
		if "8" in sub:
			print("YES")
		else:
			print("NO")