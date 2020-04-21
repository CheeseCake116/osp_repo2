#!/usr/bin/python

def union(a,b):
	lst = []
	lst1 = [int(i) for i in a]
	lst2 = [int(i) for i in b]
	lst.extend(lst1)
	lst.extend(lst2)
	lst.sort()
	length = len(lst)
	for i in range(0,length-1):
		if (lst[i] == lst[i+1]):
			lst.pop(i+1)
		if (i+1 == len(lst)-1):
			break

	return lst

def intersection(a,b):
	lst = []
	for x in a:
		for y in b:
			if (x == y):
				lst.insert(0,int(x))
	lst.sort()
	return lst
