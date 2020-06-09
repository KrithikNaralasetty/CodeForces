#987A in codeforces
gems = {
	"purple":"Power",
	"green":"Time",
	"blue":"Space",
	"red":"Reality",
	"orange":"Soul",
	"yellow":"Mind"
}
no_gems = 6
n = int(input())
times = 6-n
if times==0:
	print("0")
else:
	for i in range(n):
		gem = input()
		if gem in gems.keys():
			del gems[gem]
	print(times)
	for i in gems.keys():
		print(gems[i])