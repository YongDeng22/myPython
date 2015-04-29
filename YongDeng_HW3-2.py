#*****************************************************************************************
	#CSCI 6651
	#Homework 3 Program 2
	#Author: Yong Deng
	#Since:  4-28-2015
	# This program is to calculate the frequency of a word in a list.
#*****************************************************************************************

def count_frequency( myList ):
	freq_dic = { }
	for word in myList:
		if word not in list( freq_dic.keys() ):
			freq_dic.update( {word: 1 } )
		else:
			freq_dic.update( {word: freq_dic[word] + 1} )
	return freq_dic

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]

print (count_frequency(mylist))

#-----------------------------------------------------------------------------------------------------------------
# Sample outputs
#-----------------------------------------------------------------------------------------------------------------

# Yongs-MBP-5:~ yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng_HW3-2.py 
# {'one': 2, 'eleven': 3, 'seven': 1, 'two': 2, 'three': 2}