i,r,k = map(int,input().split())
count=0
for s in range(i,r+1):
    if s%k==0:
        count=count+1
print(count)