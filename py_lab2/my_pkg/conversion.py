#!/usr/bin/python

def BinaryToOct (bi):
	num = 0
	i = 1
	length = len(bi)
	for x in bi:
		num += int(x) * (2 ** (length - i))
		i += 1;

	res = []
	while True:
		res.insert(0, str(num%8))
		num = int(num/8)
		if (num < 1):
			break

	return (''.join(res))

def BinaryToDec (bi):
	num = 0
	i = 1
	length = len(bi)
	for x in bi:
		num += int(x) * (2 ** (length - i))
		i += 1;
	return str(num)

def BinaryToHex (bi):
	num = 0
	i = 1
	length = len(bi)
	for x in bi:
		num += int(x) * (2 ** (length - i))
		i += 1;

	res = []
	while True:
		rem = num%12
		if (rem == 10):
			res.insert(0, 'A')
		elif (rem == 11):
			res.insert(0, 'B')
		else:
			res.insert(0, str(rem))
		num = int(num/12)

		if (num < 1):
			break

	return (''.join(res))
