#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 2
	#Security Scanner
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to scan a file contains password or not.
#*****************************************************************************************


keyword = "password="
fileName = input("\nEnther the path and file name: ")
file_in = open(fileName, "r")
foundCount = 0	#count the number of passwords in the file

print("\n")
for i, line in enumerate(file_in):
	#read and enuaerate the file line by line
	if line.find(keyword) != -1:
		#if found the keyword, print the line and increment counter
		print("Found in line", i + 1, ":", line[:50])
		foundCount = foundCount + 1

#print a summary of the scan
if foundCount == 0:
	print("\nFile", fileName, "is secure.\n")
else:
	print("\nFile", fileName, "is NOT secure.", foundCount, "passwords were found.\n")


#-----------------------------------------------------------------------------------------------------------------
# Sample outputs
#-----------------------------------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4 yongdeng$ python3 securityScanner.py

# Enther the path and file name: password.txt


# Found in line 3 : password="aaa"

# Found in line 5 : password="bbb"

# Found in line 7 : password=


# File password.txt is NOT secure. 3 passwords were found.

# Yongs-MBP-5:YongDeng_HW4 yongdeng$ 

#*************************************************
# Below is the content of file password.txt:
	# abc
	# def
	# password="aaa"
	# ghi
	# password="bbb"
	# password
	# password=
	# ="ccc"

