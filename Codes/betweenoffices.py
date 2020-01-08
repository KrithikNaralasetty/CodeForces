#867A in codeforces
n = int(input())
stof = 0
ftos = 0
days = list(char for char in input())
city = days[0]
for nextcity in days:
	if city != nextcity:
		if city == "S":
			stof += 1
		elif city == "F":
			ftos += 1
		city = nextcity
if stof>ftos:
	print("YES")
else:
	print("NO")