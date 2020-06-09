#1092B in codeforces
n = int(input())
students = list(map(int,input().split()))
problems = 0
students.sort()
for i in range(0,n,2):
	problems += students[i+1]-students[i]
print(problems)