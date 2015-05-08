#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 4
	#readUserData.py
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to read data in shelve.
#*****************************************************************************************

import shelve

def readData(user):
	userData = {}
	for name, info in user.items():
		#iterate shelve, read data and store in dictionary
		userData[name] = info
	return userData