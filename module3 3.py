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
    y = input("Enter a character: ")

    if y in ('a', 'e', 'i', 'o', 'u'):
        print(y, "is a Vowel")
    else:
        print(y,"is a constant")

if __name__ == '__main__':
    main()
