#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 4
	#userData.py
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to store data using shelve.
#*****************************************************************************************

import shelve
import readUserData

user = shelve.open("User")
while True:
	name = input("Enter the name: ")
	if not name:	#if no name entered, end input
		break
	age = input("Enter the age: ")
	countryOfOrigin = input("Enter the country of origin: ")

	#store data in shelve, name is key, and (age, countryOfOrigin) as value 
	user[name] = (age, countryOfOrigin)	 

userData = readUserData.readData(user)	#read data back from shelve
print(userData)

user.clear()	#clear data
user.close()	#close shelve


#=========================================================================================
# Sample outputs
#-----------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW4/Assignment-4/userData.py 
# Enter the name: a
# Enter the age: 1
# Enter the country of origin: aaa
# Enter the name: b
# Enter the age: 2
# Enter the country of origin: bbb
# Enter the name: c
# Enter the age: 3
# Enter the country of origin: ccc
# Enter the name: d
# Enter the age: 4
# Enter the country of origin: ddd
# Enter the name: 
# {'c': ('3', 'ccc'), 'd': ('4', 'ddd'), 'b': ('2', 'bbb'), 'a': ('1', 'aaa')}
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ 

