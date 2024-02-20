n=5
length=2*n+1

i=0
x=-1
while i<length:
    if i<=length//2:
        x+=1
        print(x,end=' ')
        i+=1
    else:
        x-=1
        print(x,end=' ')
        i+=1
