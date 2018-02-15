#-------------------------------------------------------------------------------
# Name:        module3
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
     n=int(input("Enter a number: "))
     sum1 = 0
     while(n > 0):
          sum1=sum1+n
          n=n-1
     print("The sum of first n natural numbers is",sum1)
if __name__ == '__main__':
    main()
