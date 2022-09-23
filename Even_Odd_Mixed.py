n=int(input())
r=n%10
r1=n//10
p1=r1%10
p2=r1//10
s1=p1%10
s2=p1//10
if r%2==0 and p1%2==0 and s1%2==0:
    print("Even")
elif r%2==1 and p1%2==1 and s1%2==1:
    print("Odd")
else:
    print("Mixed")