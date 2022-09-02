import math
x,y,m = map(int,input().split())
a=math.pow(x,y)
b=a%m
print(int(b))