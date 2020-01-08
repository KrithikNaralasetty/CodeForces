#1005A in codeforces
n = int(input())
stairs = list(map(int,input().split()))
count = 1
b = []
j = 0
for i in range(0,n-1):
	if i!=0 and stairs[i] == 1:
		count+=1
	if stairs[i+1] == 1:
		b.append(stairs[i])
		j+=1
count = 1+len(b)
print(count)
for i in range(0,j):
	print(b[i],end = " ")
print(stairs[n-1])