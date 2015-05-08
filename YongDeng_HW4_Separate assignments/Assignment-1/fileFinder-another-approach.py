#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 1
	#File finder using another approcah
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to find a file in a path.
#*****************************************************************************************

import os
import fnmatch

def fileFinder(start_dir, fileName):
	found = 0	#track whether the file is found
	for dirpath, dirs, files in os.walk(start_dir):
		for single_file in files:
			if fnmatch.fnmatch(single_file, fileName):
				print("\n>>The file is found at:",os.path.join(dirpath, single_file), "\n")
				found = 1
	return found

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
# Yongs-MBP-5:YongDeng_HW4 yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW4/fileFinder-another-approach.py

# 	Yong Deng    Assignment 4
# 		File Finder
# ***************************************************

# Enter the inital path: /Users/yongdeng/Documents/CS

# Enther the file name: YongDeng_HW2.py

# >>The file is found at: /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW2.py 

# Yongs-MBP-5:YongDeng_HW4 yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW4/fileFinder-another-approach.py

# 	Yong Deng    Assignment 4
# 		File Finder
# ***************************************************

# Enter the inital path: /Users/yongdeng/Documents/CS

# Enther the file name: aaaaa

# File aaaaa is not found.

# Yongs-MBP-5:YongDeng_HW4 yongdeng$ 