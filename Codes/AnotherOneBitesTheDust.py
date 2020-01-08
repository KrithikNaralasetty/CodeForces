#1148A in codeforces
a,b,c = map(int,input().split())
x= min(a,b)
length = x*2
length += c*2
if x<a or x<b:
	length+=1
print(length)