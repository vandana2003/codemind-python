n=int(input())
a=n%10
a1=n//10
b=a1%10
b1=a1//10
c=b1%10
c1=b1//10
d=c1%10
d1=c1//10
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else:
    print(d)