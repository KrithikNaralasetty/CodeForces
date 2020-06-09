#1095A in codeforces
n = int(input())
cipher = input()
message=""
i,ind=1,0
while ind<n:
	message+=cipher[ind]
	ind+=i
	i+=1
print(message)