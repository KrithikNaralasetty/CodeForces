n,k = map(int,input().split())
scores = list(map(int,input().split()))
marks = scores[k-1]
passed = [x for x in scores if x>=marks and x>0]
print(len(passed))