#*****************************************************************************************
# CSCI 6651
# Homework 8 Task 2 Integer Division
#
# YongDeng_HW8_integer_division.py
# Author: Yong Deng
# Since: 6-1-2015
# This program lets the user answer integer division questions.
#*****************************************************************************************

from random import randrange

def integer_division():
	while (True):
		b = randrange(10)
		a = randrange(10) * b
		while (a == 0 and b == 0):
			a = randrange(20)
			b = randrange(20)
		if ((a != 0 and b == 0) or (a != 0 and a < b)):
				a,b = b,a			
		try:
			answer = int(input(str(a)+"/"+str(b)+"="))
			if (answer == a//b):
				print("CORRECT")
			else:
				print("INCORRECT")
		except ValueError:
			print("Please enter Integers Only!")
		except Exception as e:
			print("Error occured")
			print(type(e))

print("INTEGER DIVISIONS")
integer_division()

#=============================================================
#Sample output
#
# INTEGER DIVISIONS
# 12/2=6
# CORRECT
# 20/5=2
# INCORRECT
# 0/9=0
# CORRECT
# 24/6=r
# Please enter Integers Only!
# 0/4=12
# INCORRECT
# 20/4=dfsdfsedsfdsdsfsdfdsfdsfdsfdsfds
# Please enter Integers Only!
# 18/6=3
# CORRECT
# 12/3=4
# CORRECT
# 0/4=y
# Please enter Integers Only!