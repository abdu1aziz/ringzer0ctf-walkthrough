#!/usr/share/python2.7
#
#
# Author: Abdul Aziz
#


file_name = open('challenge_70.txt', 'r')
flag = []

for lines in file_name.readlines():
	flag.append(lines[0:1].rstrip("\n"))

for n in flag:
	if n == '':
		flag.remove('')
for i in flag:
	print(i, end="")

