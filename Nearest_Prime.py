t = int(input())
for i in range(t):
    n=int(input())
    a=n
    b=n
    while True:
        is_prime = True
        for i in range(2,int(a**0.5)+1):
            if a % i == 0:
                is_prime = False
                break
        if is_prime == True:
            break
        else:
                a+=1
    while True:
        is_prime1 = True
        for i in range(2,int(b**0.5)+1):
            if b % i == 0:
                is_prime1 = False
                break
        if is_prime1 == True:
            break
        else:
                b-=1
    
    x = a-n
    y=  n-b
    if x<y :
        print(a)
    elif x>y:
        print(b)
    else:
            if a>b:
                print(b)
            else:
                print(a)