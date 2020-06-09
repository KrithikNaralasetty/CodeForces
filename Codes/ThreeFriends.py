#1272A in codeforces
def move(x,y):
	if x > y:
		y += 1
	elif x<y:
		y -= 1
	return y
t = int(input())
for _ in range(t):
	a,b,c = map(int,input().split())
	mean = (a+b+c)//3
	a = move(mean,a)
	b = move(mean,b)
	c = move(mean,c)
	diff = abs(a-b) + abs(b-c) + abs(c-a)
	print(diff)