#266A in python
n = int(input())
s = input()
removes = 0
for i in range(n):
	st = s[i:i+2]
	if st == "RR" or st == "GG" or st == "BB":
		removes += 1
print(removes)