s=list('{{{}{}')

count=0
for i in s:
    if i=='{':
        count+=1
    else:
        count-=1
    if count<0:
        break
if count==0:
    print("Valid")
else:
    print("Not Valid")
