#*****************************************************************************************
	#CSCI 6651
	#Homework 3 Program 1
	#Author: Yong Deng
	#Since:  4-28-2015
	# This program is to calculate the total ear number of bunnies. A bunny with an odd
	# number has two ears, while a bunny with an even number has three ears.
	# The user is prompted to enter the number of bunnies. The program will calculate and
	# print the total number of ears.
#*****************************************************************************************

#function doing calculatation using recursion
def bunnyEars2(n):
	if n <= 0:	#base condition
		return 0
	elif n % 2 == 1:	#bunny with an odd number has two ears
		earNum = 2
	elif n % 2 == 0:	#bunny with an even number has three ears
		earNum = 3
	return bunnyEars2(n - 1) + earNum

while (True):
	bunnyNum = int(input("\nEnter the number of bunnies: "))
	if bunnyNum == 0:
		print("BunnyEars2(0) -> 0")
	else:
		print("BunnyEars2(" + str(bunnyNum) + ") ->", bunnyEars2(bunnyNum))

#-----------------------------------------------------------------------------------------------------------------
# Sample outputs
#-----------------------------------------------------------------------------------------------------------------

# Yongs-MBP-5:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW3-1.py 

# Enter the number of bunnies: 0
# BunnyEars2(0) -> 0

# Enter the number of bunnies: 1
# BunnyEars2(1) -> 2

# Enter the number of bunnies: 2
# BunnyEars2(2) -> 5

# Enter the number of bunnies: 3
# BunnyEars2(3) -> 7

# Enter the number of bunnies: 4
# BunnyEars2(4) -> 10

# Enter the number of bunnies: 5
# BunnyEars2(5) -> 12

# Enter the number of bunnies: 6
# BunnyEars2(6) -> 15

# Enter the number of bunnies: 7
# BunnyEars2(7) -> 17

# Enter the number of bunnies:             
