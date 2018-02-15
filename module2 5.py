#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Guest
#
# Created:     14/02/2018
# Copyright:   (c) Guest 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    print("enter three numbers:")

a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
    print(a, " is largest")
elif b>a and b>c:
    print(b, " is largest")
else:
    print(c, " is largest")

if __name__ == '__main__':
    main()
