
#*****************************************************************************************
# CSCI 6651
# Homework 9 Task 2
#
# YongDeng_HW9-2.py
# Author: Yong Deng
# Modified from Gula's program
# Since: 6-12-2015
# This program fetches data from the web and storee the data into a databse.
#*****************************************************************************************


import sqlite3
from wsgiref.simple_server import make_server

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def hello_world_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)

	conn = sqlite3.connect("zoo.sqlite")
	cursor = conn.cursor()

	#Processing request using POST method
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded:"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		cursor.execute("insert into animal_count(name, count) values(?, ?)", (form_vals["animal"], form_vals["count"]))
		for item in form_vals.keys():
			print (item + ": " + form_vals[item])
			message += "<br/>"+item + " = " + form_vals[item]
	
	#Processing request using GET method
	if (environ['REQUEST_METHOD'] == 'GET' and len(environ['QUERY_STRING'])):
		message += "<br> Your data has been recieved:"
		for param in environ['QUERY_STRING'].split("&"):
			message += "<br>"+param
		l = environ['QUERY_STRING'].split("&")
		cursor.execute("insert into animal_count(name, count) values(?, ?)", (l[0].split("=")[1], l[1].split("=")[1]))

	conn.commit()
	conn.close()

	message += "<h1>Welcome to the Zoo</h1>"

	#Building form using POST method
	message += "<br><h3>POST&nbspmethod</h3>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"

	#Building form using GET method
	message += "<br><h3>GET&nbspmethod</h3>"
	message += "<form method='GET'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"

	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()


