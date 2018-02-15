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
    year = int(input("Please Enter the Year Number you wish: "))

    if (year%400 == 0):
             print("%d is a Leap Year" %year)
    elif (year%100 == 0):
            print("%d is Not the Leap Year" %year)
    elif (year%4 == 0):
            print("%d is a Leap Year" %year)
    else:
              print("%d is Not the Leap Year" %year)

if __name__ == '__main__':
    main()
