#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Guest
#
# Created:     20/02/2018
# Copyright:   (c) Guest 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
13
def main():
    pass
a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Yes")
else:
    print("No")

if __name__ == '__main__':
    main()

