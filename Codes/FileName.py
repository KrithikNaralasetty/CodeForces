#978B in codeforces
n = int(input())
file = input()
flag = 0
removes = 0
for i in range(n):
	if file[i]=='x':
		if i<=n-3:
			sub = file[i:i+3]
			if sub == 'xxx':
				flag = 1
				removes+=1
print(removes)