#711A in codeforces
n = int(input())
possible = "NO"
bus = []
for _ in range(n):
	bus.append(list(map(str,input().split('|'))))
	if possible == "NO":
		if "OO" == bus[_][0]:
			possible ="YES"
			bus[_][0]="++"
		elif "OO" == bus[_][1]:
			possible = "YES"
			bus[_][1]="++"
print(possible)
if possible == "YES":
	for i in bus:
		print(i[0]+"|"+i[1])