revlist
a=int(input("enter a number of elements in list"))
lst=[]
print("enter the list element")
for i in range(a):
    b=int(input())
    lst.append(b)
print(lst)
print("reversed list is")
lst2=[]
for e in lst:
    lst2.insert(0,e)
print(lst2)
