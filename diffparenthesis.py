s=list('{}}}')
top=-1
stack=[]
for i in s:
    if top==-1 or i=='{' or i=='[' or i=='(':
        top+=1
        stack+=[i]
    elif i=='}' and stack[top]=='{':
        stack.pop()
        top-=1
    elif i==']' and stack[top]=='[':
        stack.pop()
        top-=1
    elif i==')' and stack[top]=='(':
        stack.pop()
        top-=1

if len(stack)==0:
    print('Matching')
else:
    print('Not matching')
