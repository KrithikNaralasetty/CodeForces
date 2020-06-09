#245A in codeforces
n = int(input())
x_a,y_a,x_b,y_b = 0,0,0,0
for _ in range(n):
	t,x,y = map(int,input().split())
	if t == 1:
		x_a+=x
		y_a+=y
	elif t == 2:
		x_b+=x
		y_b+=y
if x_a>=y_a:
	server_a = "LIVE"
else:
	server_a = "DEAD"
if x_b>=y_b:
	server_b = "LIVE"
else:
	server_b = "DEAD"
print(server_a)
print(server_b)