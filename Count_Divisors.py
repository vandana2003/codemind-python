i,r,k=map(int,input().split())
c=0
for s in range(i,r+1):
    if s%k==0:
        c+=1
print(c)