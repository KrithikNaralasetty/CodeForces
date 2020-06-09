#994A in codeforces
n,m = map(int,input().split())
seq = list(map(int,input().split()))
fingers = list(map(int,input().split()))
password = []
for i in seq:
	if i in fingers:
		password.append(i)
for i in password:
	print(i,end = " ")