#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest
#
# Created:     15/02/2018
# Copyright:   (c) Guest 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def main():
    pass
try:
	n=int(input())
	sum=0
	for i in range(1,n+1):
		sum=sum+i
	print(sum)
except:
	print("Enter numbers alone")
if __name__ == '__main__':
    main()
