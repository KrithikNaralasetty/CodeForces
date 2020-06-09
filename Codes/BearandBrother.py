#791A in code forces
a,b = map(int,input().split())
years = 0
while a<=b:
	years+=1
	a = a*3
	b = b*2
print(years)