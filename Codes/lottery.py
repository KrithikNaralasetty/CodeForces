#996A in codeforces
n = int(input())
notes = [100,20,10,5,1]
bills = 0
while n>0:
	a = notes[0]
	if n>=a:
		z = n//a
		bills+=z
		n = n-(a*z)
	notes.remove(a)
print(bills)