#*****************************************************************************************
	#CSCI 6651
	# Homework 5 File Traverse
	# Building a search engine
	# unh_crawler.py
	# Author: Yong Deng
	# Modified from Gula's program.
	# Since:  5-14-2015
	# This program is a web crawler that fetches "title", "keyword" and "description" 
	# content from "www.newhaven.edu" website. The retrieved data are preprocessed 
	# and combined with that from data_load.py. 
	# In addition to the orignal two parameters, an additional parameter "description"
	# was used for searching.
	#
	# To preprocess local file and the web, run this program first. It will create
	# a file named "raw_data.pickle" which saves filepath/url:content pairs.
#*****************************************************************************************

import urllib.request
from urllib.error import  URLError
import re

import pickle
import shutil
import data_load

crawler_backlog = {}
fileList=data_load.fileTraverse()

def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):	#crawl maximum 100 links
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):	
		return
	else:
		crawler_backlog[url] = 1	#label links have been crawled
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)	#open webpage
		code=page.getcode()
		if(code == 200):
			content=page.read()	#read source code
			content_string = content.decode("utf-8")
			#retrieve title
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')	
			#retrieve keywords
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			#retrieve description
			regexp_description = re.compile('<meta name="description" content="(?P<description>(.*))" />')

			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)
			
			resultString = ""

			if result:
				title = result.group("title")
				resultString += " " + title
				# print(title)

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				resultString += " " + keywords
				# print(keywords)

			result = regexp_description.search(content_string, re.IGNORECASE)
			if result:
				descriptions = result.group("description")
				resultString += " " + descriptions
				# print("****",descriptions)

			fileList.append((url,resultString))

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")
	# return fileList



seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
visit_url(seed, "www.newhaven.edu")
fOut = open("raw_data.pickle", "wb")

pickle.dump(fileList, fOut)
print("\nLoaded content from both files and web.")
# print(fileList)
fOut.close()

# crawler_backlog = {}
# seed = "http://www.newhaven.edu/"
# crawler_backlog[seed]=0
# visit_url(seed, "www.newhaven.edu")
