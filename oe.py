"""
n=12

#without using modulus operetor
while(True):
    if num==0:
        print("Even")
        break
    elif(num<0):
        print("Odd")
        break
    else:
        num-=2
Logic 3

if (n//2)*2 ==n:print("Even")
else:print("Odd")

#Logic 2

num=10000

#without using modulus operetor
last=num-(num//10)*10
if last==0 or last==2 or last==4 or last==6 or last==8:
    print("Even")
else:
    print("Odd")


#Logic 4

n=123
'''
b=0
while n>0:
        n=n-2
        b+=1'''
x=n//2
while x/5!=x//5:
        x=x-1
n=n-(x*2 )
#print("even") if n==0 or n==2 or n==4 or n==6 or n==8 else print("odd")
print("even") if n in [0,2,4,6,8] else print("odd")
"""

#Logic 5

num=1234
last=num-(num//10)*10

print("Even : ",last in [0,2,4,6,8])
print("Odd : ",last in [1,3,5,7,9])

