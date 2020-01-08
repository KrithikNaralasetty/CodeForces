#1080A in codeforces
# 2 red, 8 blue and 5 green
n,k = map(int,input().split())
red  = (n*2)
blue = n*8
green = n*5
books = red//k + blue//k + green//k
red = red%k
blue = blue%k
green = green%k
if red>0:
	books+=1
if blue>0:
	books+=1
if green>0:
	books+=1
print(books)