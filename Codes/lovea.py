#1146A in codeforces
from math import ceil as ceil
string = list(char for char in input())
z = string.count("a")
length = len(string)
minimum = ceil(length/2)
if z>minimum:
	print(length)
else:
	print(2*z -1)