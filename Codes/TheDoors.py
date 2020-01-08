#1143A in codeforces
n = int(input())
doors = list(map(int,input().split()))
leftdoors = doors.count(0)
rightdoors = n-leftdoors
for i in range(0,n):
	if doors[i] == 0:
		leftdoors-=1
	elif doors[i] == 1:
		rightdoors-=1
	if leftdoors==0 or rightdoors ==0:
		print(i+1)
		break