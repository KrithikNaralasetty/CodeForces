#1031A in codeforces
n,m,k = map(int,input().split())
i,glided,j = n,0,m
while k>0:
	glided+=(2*i)+(2*j)-4
	i-=4
	j-=4
	k-=1
print(glided)