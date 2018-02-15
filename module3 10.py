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
    n=int(input("Enter number:"))
    count=0
    while(n>0):
        count=count+1
        n=n//10
    print("The number of digits in the number are:",count)

if __name__ == '__main__':
    main()
