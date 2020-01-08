#1139A in codeforces
n = int(input())
l = input()
count = 0
for i in range(n):
	temp = int(l[i])
	if temp%2==0:
		count+=(i+1)
# s = int(l)
# if s%2 == 0:
# 	count+=1
print(count)