#*****************************************************************************************
	#CSCI 6651
	#Homework 5 Task 4
	#
	#YongDeng-HW5-Task-4.py
	#Author: Yong Deng
	#Modified from code of Gula.
	#Since:  5-14-2015
	#This program is return weather information in response to user's query.
#*****************************************************************************************

import urllib.request
import json
from pprint import pprint
import re

# The codes commented out Below are to use regular expression for address input.
#-------------------------------------------------------------------------------------------------------------------
# address = input("\nPlease enter the city name and state such as 'new haven, ct': (ADD TWO SPACES BEFORE INPUT)")
# regex_city = re.compile(r"(?P<city>.+), .*")
# regex_state = re.compile(r".*,\s*(?P<state>\w{2})")

# city=""
# state=""
# ch_city=''

# result = regex_city.search(address, re.IGNORECASE)
# if result:
# 	city = result.group("city")
# 	print(city)

# result = regex_state.search(address, re.IGNORECASE)
# if result:
# 	state = result.group("state")
# 	print (state)
# url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "%20" + state

address = input("\nEnther the address: ")
url = "http://api.openweathermap.org/data/2.5/weather?q=" + address
page = urllib.request.urlopen(url)

content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)

# print(json_data)
# print(json_data["coord"])
# print(json_data["coord"]["lat"])

print("\nThe weather of", json_data["name"], ":", json_data["weather"][0]["description"])
print("\nThe temperature is", "%.1f" %(json_data["main"]["temp"]-273), "degree.\n")
pprint(json_data)
print()

# =========================================================================================
# Sample output
# =========================================================================================

# Yongs-MBP-5:myPython yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng-HW5-Task-4.py 

# Enther the address: branford, ct

# The weather of Branford : Sky is Clear

# The temperature is 13.0 degree.

# {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': 41.28, 'lon': -72.81},
#  'dt': 1431660742,
#  'id': 5283054,
#  'main': {'grnd_level': 1032.7,
#           'humidity': 53,
#           'pressure': 1032.7,
#           'sea_level': 1040.53,
#           'temp': 286.044,
#           'temp_max': 286.044,
#           'temp_min': 286.044},
#  'name': 'Branford',
#  'sys': {'country': 'United States of America',
#          'message': 0.0146,
#          'sunrise': 1431682326,
#          'sunset': 1431734586},
#  'weather': [{'description': 'Sky is Clear',
#               'icon': '01n',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 211.502, 'speed': 3.31}}

# Yongs-MBP-5:myPython yongdeng$ python3 /Users/yongdeng/Documents/CS/UNH\ assignments/CSCI\ 6651\ python/myPython/YongDeng-HW5-Task-4.py 

# Enther the address: new haven, ct

# The weather of New Haven : Sky is Clear

# The temperature is 12.4 degree.

# {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': 41.31, 'lon': -72.92},
#  'dt': 1431659258,
#  'id': 4839366,
#  'main': {'grnd_level': 1025.08,
#           'humidity': 49,
#           'pressure': 1025.08,
#           'sea_level': 1040.36,
#           'temp': 285.394,
#           'temp_max': 285.394,
#           'temp_min': 285.394},
#  'name': 'New Haven',
#  'sys': {'country': 'United States of America',
#          'message': 0.0167,
#          'sunrise': 1431682349,
#          'sunset': 1431734617},
#  'weather': [{'description': 'Sky is Clear',
#               'icon': '01n',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 202.002, 'speed': 2.51}}

# Yongs-MBP-5:myPython yongdeng$ 
