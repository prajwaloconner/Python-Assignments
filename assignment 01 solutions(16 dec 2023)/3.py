n=50
a=0
b=1
s=0
print("0")
for i in range(50):
    s=a+b
    if(s>50):
        break
    print(s)
    b=a
    a=s


    