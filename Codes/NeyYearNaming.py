#1284A in codeforces
n,m = map(int,input().split())
first = list(map(str,input().split()))
last = list(map(str,input().split()))
t = int(input())
for _ in range(t):
	x = int(input())
	a = (x%n) - 1
	b = (x%m) -1
	string = first[a]+last[b]
	print(string)