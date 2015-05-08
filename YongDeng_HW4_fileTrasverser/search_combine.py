#*****************************************************************************************
	#CSCI 6651
	#Homework 4 File Traverse
	#Building a search engine
	#search_combine.py
	#Author: Yong Deng
	#Since:  5-7-2015
	#This program is a to call other modules to perform searching.
#*****************************************************************************************

import data_load
import indexer
import searcher

data = indexer.processData("raw_data.pickle", "fortune_shelve")
searcher.search("fortune_shelve")

#=================================================================================================================
# Sample outputs
#=================================================================================================================
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ python3 search_combine.py 

# query:the and was or if

# Performing AND search for: {'was', 'the', 'if'} 

# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune9.log

# Execution time: 231 

#-----------------------------------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ python3 search_combine.py 

# query:go or give

# Performing OR search for: {'give', 'go'} 

# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune1.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune1.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune10.txt

# Execution time: 109 

#-----------------------------------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ python3 search_combine.py 

# query:down

# Performing AND search for: {'down'} 

# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune13.log

# Execution time: 133 

#-----------------------------------------------------------------------------------------------------------------
# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ python3 search_combine.py 

# query:the

# Performing AND search for: {'the'} 

# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune2.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune4.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune12.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune16.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune18/fortune19/fortune20/fortune20.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune15.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune8.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune8.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune10.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune7.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune17.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune11.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune18/fortune19/fortune19.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune18/fortune19/fortune20/fortune20.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune9.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune3.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune13.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune10.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune17.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune4.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune9.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune1.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune14.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune2.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune15.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune13.log
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW4_fileTrasverser/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune6.txt

# Execution time: 594 

# Yongs-MBP-5:YongDeng_HW4_fileTrasverser yongdeng$ 
