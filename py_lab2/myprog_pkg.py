#!/usr/bin/python
import sys
import my_pkg

while True:
	choice = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))

	if (choice == 1):
		str = input("Input binary number : ")
		print("=> OCT>", my_pkg.BinaryToOct(str))
		print("=> DEC>", my_pkg.BinaryToDec(str))
		print("=> HEX>", my_pkg.BinaryToHex(str))
	elif (choice == 2):
		str1 = input("1st list: ")
		str1 = str1.strip('[]')
		str1 = str1.replace(" ","")
		lst1 = str1.split(',')

		str2 = input("2nd list: ")
		str2 = str2.strip('[]')
		str2 = str2.replace(" ","")
		lst2 = str2.split(',')

		print("=> union", my_pkg.union(lst1,lst2))
		print("=> intersection", my_pkg.intersection(lst1,lst2))
	else:
		print("exit the program...")
		sys.exit()
