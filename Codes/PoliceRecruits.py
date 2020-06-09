#427A in codeforces
n = int(input())
activities = list(map(int,input().split()))
police = 0
crimes = 0
for i in activities:
	if i<0:
		if police == 0:
			crimes+=1
		else:
			police+=i
	elif i>0:
		police+=i
print(crimes)