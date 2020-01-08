#835 in codeforces
s,v1,v2,t1,t2 = map(int,input().split())
time_for_first = s*v1 + 2*t1
time_for_second  = s*v2 + 2*t2
if time_for_first<time_for_second:
	print("First")
elif time_for_second==time_for_first:
	print("Friendship")
else:
	print("Second")