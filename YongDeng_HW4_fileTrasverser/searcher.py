#*****************************************************************************************
	#CSCI 6651
	#Homework 4 File Traverse
	#Building a search engine
	#searcher.py
	#Author: Yong Deng
	#Since:  5-7-2015
	#This program is a to perform searching.
	#Users are prompted to enter the query. The program will determine the kind of search
	#to perform. Then the program will search the words in the query against the index
	#created in indexer.py.
#*****************************************************************************************

import data_load
import indexer
import shelve

def search(fortune_shelve):
	#--------------------------------------------------------------------------------------------
	#processing query
	
	# print(word_dic["go"])
	word_dic = shelve.open(fortune_shelve)
	
	while(True):
		#loop to prompt for and validate query 
		query = input("\nquery:").lower()	#prompt the user to enter query and convert to lower case
		query = set(query.split())	#split the query and convert to set

		#determine what operation to perform
		if ("and" not in query and "or" in query):
			operation = "OR"
		else:
			operation = "AND"

		#remove any "or" or/and "and" in the query
		if ("and" in query):
			query.remove("and")
		if ("or" in query):
			query.remove("or")

		#validate query. If query empty or only contains boolean operators
		if len(query) > 0:
			break
		else:
			print("ERROR! Query cannot be empty.")


	#--------------------------------------------------------------------------------------------
	#searching
	print("\nPerforming", operation, "search for:", query, "\n")

	from datetime import datetime
	dt1 = datetime.now()	# start time

	foundSet = set()	#initialize set container which holds all the hits

	if operation == "OR":
		#perform OR search
		for q in query:
			foundSet = foundSet | set(word_dic[q])
	else:
		foundSet = indexer.finalList;
		#perform "AND" search
		for q in query:
			if q not in (word_dic).keys():
				foundSet = set()	#if any of the key is not found, set foundSet to empty and end search
				break
			else:
				foundSet = foundSet & set(word_dic[q])	#find the hits fulfill all conditions

	if foundSet:
		#if search result is not empty, print result
		for item in foundSet:
			print(">>Found at", item)
	else:
		#if nothing found, print message
		print("\nNo match found.\n")				

	dt2= datetime.now()	#end time 

	print("\nExecution time:", dt2.microsecond-dt1.microsecond, "\n")	#calcuate running time
	word_dic.close()
