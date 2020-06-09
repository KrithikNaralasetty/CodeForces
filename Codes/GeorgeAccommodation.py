#467A in codeforces
n = int(input())
rooms = 0
for _ in range(n):
	a,b = map(int,input().split())
	if a+2<=b:
		rooms+=1
print(rooms)