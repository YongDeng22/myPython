#*****************************************************************************************
	#CSCI 6651
	#Homework 4 File Traverse
	#Building a search engine
	#data_load.py
	#Author: Yong Deng
	#Since:  5-7-2015
	#This program is to pre-processing data.
	#This program traverses a folder, search for .log and .txt files, save the 
	#content and absolute path of each file as a single tuple. All of these data are
	#then saved in a list for future searching.
#*****************************************************************************************

import os
import fnmatch
import pickle
import shutil

def fileTraverse():
	start_dir = "fortune1"
	fileList = []	#used to store processed data list
	for dirpath, dirs, files in os.walk(start_dir):
		#traverse folder and processing data
		for single_file in files:
			if fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log"):
				filePath = os.path.abspath(os.path.join(dirpath, single_file))
				fIn = open(filePath, "rb")	#binary read
				print("Creating a tuple with", single_file, "content and", filePath, "path\n")
				fileList.append((fIn.read(), filePath))
				fIn.close()
	fOut = open("raw_data.pickle", "wb")
	pickle.dump(fileList, fOut)	#binary write using pickle
	fOut.close()
