#1220A in codeforces
from collections import Counter as counter
n = int(input())
output = ""
letters = list(char for char in input())
z = letters.count("n")
for i in range(z):
	output+="1 "
n -= z*3
x = n//4
for i in range(x):
	output+="0 "
print(output)