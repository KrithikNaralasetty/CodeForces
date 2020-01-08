#1272D in codeforces
n = int(input())
arr = list(map(int,input().split()))
i = 0
l = 0
flag = 1
while i < n:
	if flag == 1:
		j = i+1
		if arr[j]>arr[i]:
			flag = 1
			i+=1
		else:
			flag = 0
	elif flag == 0:
		arr.remove(arr[i])
		break

print(l)