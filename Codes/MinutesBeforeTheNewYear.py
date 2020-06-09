#1283A in codeforces
t = int(input())
for _ in range(t):
	h,m = map(int,input().split())
	time = 1440 - (60*h) - m
	print(time)