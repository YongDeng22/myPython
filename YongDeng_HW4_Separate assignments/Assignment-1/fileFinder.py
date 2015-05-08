#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 1
	#File finder
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to find a file in a path.
#*****************************************************************************************

import os

#-----------------------------------------------------------------------------------------
#function definition
def fileFinder(path, fileName):
	iPath = path	#hold the initial path
	found = 0		#To track whether it is found. if found laerger than 0, otherwise 0
	if os.path.isfile(path):
		#if the path itself if a file
		if os.path.split(path)[1] == fileName:
			print(path, "\n")
			found = found + 1
	elif os.path.isdir(path):
		#if the path is a directory
		l=os.listdir(path)
		for f in l:
			#loop through the files and directories in the path
			path = iPath
			if os.path.isfile(os.path.join(path,f)):
				#if the path is a file
				if f == fileName:
					print("\n>>The file is found at:",os.path.join(path,f), "\n")
					found = found + 1	#if file found, increment 1
			elif os.path.isdir(path):
				#if the path is a directory, recursively travers the path
				path = os.path.join(path,f)
				found = found + fileFinder(path, fileName)
	return found	#return found so as to track whether the file is found or not

#-----------------------------------------------------------------------------------------
print("\n\tYong Deng    Assignment 4")
print("\t\tFile Finder")
print("***************************************************")

initPath = input("\nEnter the inital path: ")
fileToFind = input ("\nEnther the file name: ")
fileFound = fileFinder(initPath, fileToFind)
if fileFound == 0:
	print("\nFile", fileToFind, "is not found.\n")

#-----------------------------------------------------------------------------------------------------------------
# Sample outputs
#-----------------------------------------------------------------------------------------------------------------
# Yongs-MBP-5:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW4/fileFinder.py 

# 	Yong Deng    Assignment 4
# 		File Finder
# ***************************************************

# Enter the inital path: /Users/yongdeng/Documents/CS

# Enther the file name: YongDeng_HW2.py

# >>The file is found at: /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW2.py 

#-----------------------------------------------------------------------------------------------------------------

# Yongs-MBP-5:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW4/fileFinder.py 

# 	Yong Deng    Assignment 4
# 		File Finder
# ***************************************************

# Enter the inital path: /Users/yongdeng/Documents/CS

# Enther the file name: abcd.py

# File abcd.py is not found.

# Yongs-MBP-5:~ yongdeng$ 

