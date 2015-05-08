#*****************************************************************************************
	#CSCI 6651
	#Homework 4 Separate Assignments Program 3
	#File finder
	#Author: Yong Deng
	#Since:  5-7-2015
	# This program is to compare the efficiency of dictionary and shelve.
#*****************************************************************************************
import shelve
from datetime import datetime

d = {"a":(1,2,3), "b":(4,5,6), "c": "shelve", "d": "dictionary", "e": {1:2, 2:3, 3:4}}

s = shelve.open("testShelve")
s["a"] = (1, 2, 3)
s["b"] = (4, 5, 6)
s["c"] = "shelve"
s["d"] = "dictionary"
s["e"] = {1: 2, 2: 3, 3:4}

#-----------------------------------------------------------------------------------------
#process dictioanry
print("\nProcessing Dictionary:\n")
dt1 = datetime.now()
for key, value in d.items():
	print(key, ":", value)
dt2 = datetime.now()
dicT = dt2-dt1

#-----------------------------------------------------------------------------------------
#process shelve
print("\nProcessing Shelve:\n")
dt3 = datetime.now()
for key, value in s.items():
	print(key, ":", value)
s.close()
dt4 = datetime.now()

#-----------------------------------------------------------------------------------------
#print result
shelT = dt4 - dt3
print("Dictionary:", dicT, "\nShelve:", shelT, "\n")
if dicT < shelT:
	print("Dictionary is faster.\n")
else:
	print("Shelve is faster.\n")

#=========================================================================================
# Sample outputs
#-----------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4 yongdeng$ python3 dic_shiv_which_faster.py

# Processing Dictionary:

# c : shelve
# b : (4, 5, 6)
# a : (1, 2, 3)
# e : {1: 2, 2: 3, 3: 4}
# d : dictionary

# Processing Shelve:

# b : (4, 5, 6)
# d : dictionary
# a : (1, 2, 3)
# c : shelve
# e : {1: 2, 2: 3, 3: 4}
# Dictionary: 0:00:00.000097 
# Shelve: 0:00:00.000216 

# Dictionary is faster.

# Yongs-MBP-5:YongDeng_HW4 yongdeng$ 
