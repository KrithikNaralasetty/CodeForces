#721A in codeforces
n = int(input())
groups = 0
count = 0 
lengths =[]
crossword = input()
for i in range(0,n):
	if crossword[i]=="B":
		count+=1
	else:
		if count>0:
			lengths.append(count)
			groups+=1
		count = 0
if count>0:
	groups+=1
	lengths.append(count)
print(groups)
for i in lengths:
	print(i,end = " ")