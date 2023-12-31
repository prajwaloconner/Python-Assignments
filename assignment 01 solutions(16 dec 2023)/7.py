a=int(input("enter a number"))
cnt=0
b=a
while(True):
    c=int(b/10)
    if(c>0):
        cnt+=1
        b=b/10
    else:
        break
print("digit cnt",cnt+1)