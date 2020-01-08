#723A in codeforces
houses = list(map(int,input().split()))
houses.sort()
dist = (houses[1]- houses[0]) + (houses[2]-houses[1])
print(dist)