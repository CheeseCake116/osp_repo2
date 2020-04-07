#!/usr/bin/python

num = int(input("How many numbers will you put?"))
print("Enter %d number(s): " % num)
sum = 0
for i in range(0,num):
	temp = int(input())
	sum += temp
aver = sum / num
print("average is %d" % aver)
