#1191A in codeforces
cat = {1:"A",
3:"B",
2:"C",
0:"D"
}
n = int(input())
z = n%4
if z == 0:
	print("1 "+cat[1])
elif z == 1:
	print("0 "+cat[1])
elif z == 2:
	print("1 "+cat[3])
elif z == 3:
	print("2 "+cat[1])