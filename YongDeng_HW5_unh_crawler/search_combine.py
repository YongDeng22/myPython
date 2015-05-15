#*****************************************************************************************
	#CSCI 6651
	#Homework 5 File Traverse
	#Building a search engine
	#search_combine.py
	#Author: Yong Deng
	#Since:  5-7-2015
	#This program is a to call other modules to perform searching.
#*****************************************************************************************

import indexer
import searcher


data = indexer.processData("raw_data.pickle", "fortune_web_shelve")
searcher.search("fortune_web_shelve")

#=================================================================================================================
# Sample outputs
#=================================================================================================================
# Yongs-MBP-5:YongDeng_HW5_unh_crawler yongdeng$ python3 search_combine.py

# query:new haven

# Performing AND search for: {'new', 'haven'} 

# >>Found at http://www.newhaven.edu/admissions/apply/
# >>Found at http://www.newhaven.edu/academics/resources/bursars/fall
# >>Found at http://www.newhaven.edu/about/employment/equal
# >>Found at http://www.newhaven.edu/academics/resources/registrar/
# >>Found at http://www.newhaven.edu/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/FERPA/directory/
# >>Found at http://www.newhaven.edu/292038/
# >>Found at http://www.newhaven.edu/OIT/support/
# >>Found at http://www.newhaven.edu/admissions/internationaladmissions/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/registration
# >>Found at http://www.newhaven.edu/OIT/information
# >>Found at http://www.newhaven.edu/academics/schedules
# >>Found at http://www.newhaven.edu/Veteran
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/
# >>Found at http://www.newhaven.edu/submit
# >>Found at http://www.newhaven.edu/academics/resources/
# >>Found at http://www.newhaven.edu/15/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/transcript
# >>Found at http://www.newhaven.edu/301001/
# >>Found at http://www.newhaven.edu/about/employment/directions
# >>Found at http://www.newhaven.edu/4486/WNHU/meet
# >>Found at http://www.newhaven.edu/academics/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/graduation
# >>Found at http://www.newhaven.edu/academics/resources/registrar/regulations/
# >>Found at http://www.newhaven.edu/admissions/
# >>Found at http://www.newhaven.edu/IEL/study
# >>Found at http://www.newhaven.edu/831482
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/atypical
# >>Found at http://www.newhaven.edu/about/employment/wrongful
# >>Found at http://www.newhaven.edu/292038
# >>Found at http://www.newhaven.edu/information
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/391174/
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/dean/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/forms/
# >>Found at http://www.newhaven.edu/4486/WNHU/contact/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/veterans/
# >>Found at http://www.newhaven.edu/291891
# >>Found at http://www.newhaven.edu/academics/resources/registrar/diploma
# >>Found at http://www.newhaven.edu/Spotlight
# >>Found at http://www.newhaven.edu/academics/centers
# >>Found at http://www.newhaven.edu/googlesearch/
# >>Found at http://www.newhaven.edu/top
# >>Found at http://www.newhaven.edu/about/employment/job
# >>Found at http://www.newhaven.edu/studenthandbook
# >>Found at http://www.newhaven.edu/OIT/
# >>Found at http://www.newhaven.edu/about/employment/human
# >>Found at http://www.newhaven.edu/academics/resources/registrar/staff/
# >>Found at http://www.newhaven.edu/academics/grants
# >>Found at http://www.newhaven.edu/academics/resources/bursars/student
# >>Found at http://www.newhaven.edu/online
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/online
# >>Found at http://www.newhaven.edu/academics/resources/bursars/750041/
# >>Found at http://www.newhaven.edu/4486/WNHU/djs
# >>Found at http://www.newhaven.edu/academics/resources/registrar/veterans/military
# >>Found at http://www.newhaven.edu/academics/resources/registrar/degree
# >>Found at http://www.newhaven.edu/events/
# >>Found at http://www.newhaven.edu/4486/
# >>Found at http://www.newhaven.edu/student
# >>Found at http://www.newhaven.edu/business/
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/mission/
# >>Found at http://www.newhaven.edu/admissions/gradadmissions/
# >>Found at http://www.newhaven.edu/about/visitors/
# >>Found at http://www.newhaven.edu/families/
# >>Found at http://www.newhaven.edu/301001
# >>Found at http://www.newhaven.edu/academics/lyme
# >>Found at http://www.newhaven.edu/4486/WNHU/schedule/
# >>Found at http://www.newhaven.edu/admissions/financial
# >>Found at http://www.newhaven.edu/about/IDEA/
# >>Found at http://www.newhaven.edu/news
# >>Found at http://www.newhaven.edu/about/
# >>Found at http://www.newhaven.edu/cdc/
# >>Found at http://www.newhaven.edu/supportunh/
# >>Found at http://www.newhaven.edu/about/title
# >>Found at http://www.newhaven.edu/commencement
# >>Found at http://www.newhaven.edu/301103
# >>Found at http://www.newhaven.edu/academics/resources/bursars/
# >>Found at http://www.newhaven.edu/admissions/ugrad/
# >>Found at http://www.newhaven.edu/library/common
# >>Found at http://www.newhaven.edu/public
# >>Found at http://www.newhaven.edu/4486/WNHU/
# >>Found at http://www.newhaven.edu/academics/resources/registrar/FERPA/release
# >>Found at http://www.newhaven.edu/291891/
# >>Found at http://www.newhaven.edu/library/
# >>Found at http://www.newhaven.edu/OIT/status/
# >>Found at http://www.newhaven.edu/directory/
# >>Found at http://www.newhaven.edu/Lifelong_eLearning/staff/
# >>Found at http://www.newhaven.edu/alumni/
# >>Found at http://www.newhaven.edu/lee
# >>Found at http://www.newhaven.edu/academics/resources/registrar/grading/
# >>Found at http://www.newhaven.edu/4032/
# >>Found at http://www.newhaven.edu/prospective/
# >>Found at http://www.newhaven.edu/engineering/
# >>Found at http://www.newhaven.edu/about/employment/
# >>Found at http://www.newhaven.edu/4486/WNHU/photos/
# >>Found at http://www.newhaven.edu/engineering/academic
# >>Found at http://www.newhaven.edu
# >>Found at http://www.newhaven.edu/academics/resources/registrar/FERPA/

# Execution time: 1669 

# Yongs-MBP-5:YongDeng_HW5_unh_crawler yongdeng$ python3 search_combine.py

# query:all

# Performing AND search for: {'all'} 

# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW5_unh_crawler/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune10.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW5_unh_crawler/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune13.txt
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW5_unh_crawler/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune15.txt
# >>Found at http://www.newhaven.edu/291891/
# >>Found at http://www.newhaven.edu/291891
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW5_unh_crawler/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune10/fortune11/fortune12/fortune13/fortune14/fortune15/fortune16/fortune17/fortune18/fortune19/fortune20/fortune20.txt
# >>Found at http://www.newhaven.edu/academics/resources/registrar/forms/
# >>Found at /Users/yongdeng/Documents/CS/UNH assignments/CSCI 6651 python/myPython/YongDeng_HW5_unh_crawler/fortune1/fortune2/fortune3/fortune4/fortune5/fortune6/fortune7/fortune8/fortune9/fortune9.log

# Execution time: 244 

# Yongs-MBP-5:YongDeng_HW5_unh_crawler yongdeng$ 
