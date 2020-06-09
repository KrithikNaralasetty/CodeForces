#268A in codeforces
n = int(input())
teams = {}
guest = 0
for i in range(n):
	teams[i+1] = list(map(int,input().split()))
for i in range(1,n+1):
	for j in range(1,n+1):
		if i!=j:
			if teams[i][0] == teams[j][1]:
				guest+=1
print(guest)