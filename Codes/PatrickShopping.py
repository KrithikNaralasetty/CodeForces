#599A in codeforces
d1,d2,d3 = map(int,input().split())
a = 2*(d1 + d2)
b = 2*(d2 + d3)
c = 2*(d1 + d3)
d = d1 + d2 + d3
z = min(a,b,c,d)
print(z)