def main():
    c=int(input("enter a number"))
def prime(n):
    a= True
    for i in range(2,n):
        if (n%i == 0):
            a = False
    return a
c=int(input("enter a number"))
for i in range(2,c):
       if prime(i):
           print (i)
main()