#271A in codeforces
a = [i for i in range(10)]
s = int(input())
s+=1
flag = 0
while s<=9000:
	x = a
	for i in str(s):
		if int(i) in x:
			x.remove(int(i))
		else:
			flag = 1
			break
	if flag == 1:
		s+=1
	else:
		print(s)
		break