password wala question


import re
pattern=r'[A-Za-z0-9@#$%^&+=]{8,}'
a=input("enter a password")
if(re.findall(pattern,a)):
    print("valid ")
else:
    print("invalid")