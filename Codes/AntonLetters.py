#443A in codeforces
sets = input()
n = len(sets)
elements = sets[1:n-1]
if len(elements) == 0:
	print(0)
else:
	a = len(set(map(str,elements.split(", "))))
	print(a)