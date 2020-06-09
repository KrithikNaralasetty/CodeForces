#339A in Codeforces
statement = input()
a = []
for i in statement:
	if i !='+':
		a.append(i)
a = sorted(a)
statement = ''
for i in a:
	statement+=i+'+'
print(statement[:-1])