#1285A in codeforces
from collections import Counter as c
n = int(input())
string = input()
Controls = c(string)
a = Controls["L"]
b = Controls["R"]
print(a+b+1)