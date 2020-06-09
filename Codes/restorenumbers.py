#1154A in codeforces
sums = list(map(int,input().split()))
sums.sort()
x1,x2,x3,x4 = map(int,(i for i in sums))
c = x4 - x1
b = x4 - x3
a = x4 - x2
if a+b+c == x4:
	print(str(a)+" "+str(b)+" "+str(c))