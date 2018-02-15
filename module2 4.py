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
    y = input("Enter a character: ")

    if y in ('a','b','c','d','e','f','g,','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
        print(y, "is a Alphabet")
    else:
        print(y,"is a No")


if __name__ == '__main__':
    main()
