#1173A in codeforces
x,y,z = map(int,input().split())
if x<y:
	y = y-x
	if y>z:
		upvotes = "-"
	else:
		upvotes = "?"
elif x == y:
	if z == 0:
		upvotes = "0"
	else:
		upvotes = "?"
elif x>y:
	x = x-y
	if x<=z:
		upvotes = "?"
	else:
		upvotes = "+"
print(upvotes)