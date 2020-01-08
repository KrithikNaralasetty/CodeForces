#71A in codeforces
n = int(input())
for _ in range(n):
	string = input()
	length = len(string)
	if length>10:
		st = string[0]+str(length-2)+string[-1]
	else:
		st = string
	print(st)