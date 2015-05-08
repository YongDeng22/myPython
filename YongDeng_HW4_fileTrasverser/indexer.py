#*****************************************************************************************
	#CSCI 6651
	#Homework 4 File Traverse
	#Building a search engine
	#indexer.py
	#Author: Yong Deng
	#Since:  5-7-2015
	#This program is a to further process data stored in data_load.py.
	#Each single word is indexed to the absolute path of the files which contain it. 
#*****************************************************************************************

import pickle
import os
import shelve

#-------------------------------------------------------------------------------------------
#processing data
def processData(path, fortune_shelve):
	f = open(path, "rb")	#open pickle file created in data_load.py

	#read the data which is a list of tuples in a format of (content, absolute file path)
	data_list = pickle.load(f)

	#dictioanry container for all of the words (key) and sentence number(value)	
	word_dic = shelve.open(fortune_shelve)	

	global finalList
	finalList = []	#stores all of the absolute file pathes

	for item in data_list:
	#for loop to generate dictionary and list containers
		i = item[1]	#absolute file path
		quote = item[0]	#file content
		finalList.append(i)

		words = set(quote.split())	#split file content to a set of single words
		for word in words:
			word = word.decode('utf-8').lower()	#convert binary string to lowercase regular string
			#create index which is stored in a dictionary
			if word in word_dic.keys():
				word_dic[word].append(i) 
			else:
				word_dic.update({word:[i]})
			word_dic.sync()	#synchronize shelve
	
	finalList = set(finalList)	#illiminate duplicates
	f.close()
	word_dic.close()
	# return word_dic




