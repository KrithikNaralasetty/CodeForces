#731A in codeforces
s = input()
rotations = 0
pointer = 96
for i in s:
	if ord(i)-pointer <= 12:
		rotations += abs()
	elif ord(i)-pointer>=13:
		rotations += (26-ord(i)+pointer)
	pointer = ord(i) - 1
print(rotations)