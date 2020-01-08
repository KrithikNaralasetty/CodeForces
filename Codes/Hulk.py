#705A in codeforces
n = int(input())
anagram = ["I hate ","I love "]
final = ""
for _ in range(n):
	z = _%2
	final += anagram[z]
	if _ == n-1:
		final+= "it"
	else:
		final+="that "
print(final)