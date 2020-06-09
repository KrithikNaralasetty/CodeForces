#734A in codeforces
n = int(input())
games=0
for char in input():
	if char == "A":
		games+=1
	else:
		games-=1
if games<0:
	print("Danik")
elif games>0:
	print("Anton")
else:
	print("Friendship")