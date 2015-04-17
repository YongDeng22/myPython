# CSCI 6651 Assignment 1
# Author: Yong Deng
# Since:  4/16/2015

# This program is to guess a number that a user thought of.
# The program will guess a number and ask the user whether it's the number or not.
# If not, the program will ask whether the number is larger or not.
# The user needs only to answer yes or no to each question. Otherwise, the user will be
# prompted to re-answer the question.
#----------------------------------------------------------------------------------------------

name = input("\nHi, what is your Name? ")
print("\nHello "+name+"! let's play a game!")
print("\nThink of random number from 1 to 100, and I'll try to guess it!")
play = "yes"		#whether the user want to play
count = 0		#count of guesses. When the user did not enter yes/no, it's not counted
smallerNumber = 1	#the smallest number in the range
largerNumber = 100	#the largest number in the range

while (play == "yes" and smallerNumber <= largerNumber):
	guess = (smallerNumber + largerNumber) // 2		#the number guessed
	answer = input("\nIs it " + str(guess) + "? (yes/no)")	#match? yes, otherwise no
	count = count + 1

	if answer == "yes":
		#when the program got the number, prints message, re-initializes the variables,
		#and ask the user to play again or not
		print("\nYeey! I got it in " + str(count) + " tries!\n")
		count = 0
		smallerNumber = 1
		largerNumber = 100
		play = input("\nDo you want to play more? (yes/no)")
	elif answer == "no":
		#when guess is wrong, ask whether the number is larger than guessed number or not
		isLarger = input ("\nIs the number larger than " + str(guess) + " ? (yes/no)")
		while (isLarger != "yes" and isLarger != "no"):
		#if the user entered wrong info, prompt to enter again
			isLarger = input ("\nIs the number larger than " + str(guess) + " ? (yes/no)")
		if isLarger == "yes":
			smallerNumber = guess + 1
		else:
			largerNumber = guess - 1 
	else:
		#if the user entered wrong answer (neither yes nor no), set count back to previous value
		count = count - 1 

else:
	#if the user wants to quit
	print ("\nBye-bye")

#-----------------------------------------------------------------------------------------------------------------
# Sample outputs
#-----------------------------------------------------------------------------------------------------------------
# Last login: Thu Apr 16 15:30:15 on ttys000
# Yongs-MBP:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/Yong\ Deng_HW1.py 

# Hi, what is your Name? yong

# Hello yong! let's play a game!

# Think of random number from 1 to 100, and I'll try to guess it!

# Is it 50? (yes/no)no

# Is the number larger than 50 ? (yes/no)yes

# Is it 75? (yes/no)no

# Is the number larger than 75 ? (yes/no)no

# Is it 62? (yes/no)yes

# Yeey! I got it in 3 tries!


# Do you want to play more? (yes/no)yes

# Is it 50? (yes/no)no

# Is the number larger than 50 ? (yes/no)no

# Is it 25? (yes/no)no

# Is the number larger than 25 ? (yes/no)yes

# Is it 37? (yes/no)no

# Is the number larger than 37 ? (yes/no)yes

# Is it 43? (yes/no)no

# Is the number larger than 43 ? (yes/no)no

# Is it 40? (yes/no)yes

# Yeey! I got it in 5 tries!


# Do you want to play more? (yes/no)no

# Bye-bye
# Yongs-MBP:~ yongdeng$ 

