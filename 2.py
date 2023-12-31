a=[]
n=int(input("enter mumber of elements"))
for i in range(n):
    b=int(input())
    a.append(b)
e=0
o=0
for i in range (n):
    if i%2 == 0:
        e+=1
    else:
        o+=1
print("even numbers",e,"\nodd numbers=",o)