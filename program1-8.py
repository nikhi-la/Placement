def length(n):
    if n<0:
        n=n*-1
    c=0
    while(n):
        n=n//10
        c+=1
    return c

def power10(n):
    zero=1
    while(n):
        zero=zero*10
        n-=1
    return zero
    
'''
#Program 1 output=4

n=-1234    

if n<0:
    n*=-1

last=n-(n//10)*10 # or last=n%10
print(last)

#Program 2 output=123

n=1234

exceptlast=n//10
print(exceptlast)

#Program 3 output=123477

n=1234
m=77

digitsinm=length(m)

number=n*(power10(digitsinm))+m
print(number)

'''


#Program 4 output=1277


n=-1234
m=7777777

flag=1
if n<0:
    n*=-1
    flag=-1

    
if m<0:
    m*=-1
if length(m)>=length(n):
    print(flag*m)
else:
    digitsinm=length(m)
    num=((n//power10(digitsinm))*power10(digitsinm)+m)
    print(flag*num)

'''

#Program 5 output = 1

n=1234

digitsinm=length(n)

f=n//power10(digitsinm)
print(f)



#Program 6 output=234

n=1234

digitsinm=length(n)

num=n%power10(digitsinm)
print(num)



#Program 7 Output=771234

n=1234
m=77

digitsinn=length(n)

number=m*(power10(digitsinn))+n
print(number)


#Program 8 Output=7734

n=1234
m=77
md=length(m)
nd=length(n)
num=n%power10((nd-md))

number=m*power10(length(num))+num
print(number)



#Program 9 output=127734

n=-12345 
m=7777777


flag=1
if n<0:
    n*=-1
    flag=-1

    
if m<0:
    m*=-1


nd=length(n)
if not nd%2:
    mid=nd//2
    
    f=n//power10(mid)
    f=f*power10(length(m))+m
    f=f*power10(mid)+n%power10(mid)   
    print(flag*f)
else:
    mid1,mid2=nd//2,(nd+1)//2
    f1,f2=n//power10(mid1),n//power10(mid2)
    f1,f2=f1*power10(length(m))+m,f2*power10(length(m))+m
    f1,f2=f1*power10(mid1)+n%power10(mid1),f2*power10(mid2)+n%power10(mid2)     
    print(flag*f1,',',flag*f2)
    

    
'''
    
