#734B in codeforces
a,b,c,d = map(int,input().split())
x = min(a,c,d)
a = a - x
y = min(a,b)
z = x*256 + y*32
print(z)