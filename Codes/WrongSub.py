#977A in codeforces
n,k = map(int,input().split())
while k>0:
	x = n%10
	#print(x)
	if x>=k:
		n = n-k
	elif x == 0:
		n = n//10
		k -=1
	else:
		n = n-x
	k = k-x
	#print("n is "+str(n))
	#print("k is "+str(k))
print(n)