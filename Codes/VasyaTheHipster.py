#581A in Codeforces
a,b = map(int,input().split())
hipster = min(a,b)
a = a-hipster
b = b-hipster
if b == 0:
	days = a//2
elif a == 0:
	days = b//2
print(str(hipster)+" "+str(days))