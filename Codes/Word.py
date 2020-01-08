name = input()
length = len(name)
upp = 0
low =  0
for i in name:
	if ord(i)>=97 and ord(i)<123:
		low += 1
	else:
		upp +=1
if upp>low:
	print(name.upper())
else:
	print(name.lower())