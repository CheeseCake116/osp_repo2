#!/usr/bin/python

f1 = f2 = 1
num = int(input("Enter number of fibo: "))
if num > 0 :
	print(f1)
if num > 1 :
	print(f2)
for i in range(0,num-2):
	temp = f1 + f2
	f1 = f2
	f2 = temp
	print(f2)
if num == 1 :
	print("F{0} = {1}".format(num,f1))
if num > 1 :
	print("F{0} = {1}".format(num,f2))
