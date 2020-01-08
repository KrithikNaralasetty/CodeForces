#431A in codeforces
calory = list(map(int,input().split()))
game = input()
spent = 0
for i in game:
	spent+=calory[(int(i)-1)]
print(spent)