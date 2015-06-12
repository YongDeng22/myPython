
#*****************************************************************************************
# CSCI 6651
# Homework 9 Task 1
#
# YongDeng_HW9-1.py
# Author: Yong Deng
# Since: 6-12-2015
# This program monitors the system info of the current computer.
#*****************************************************************************************


import psutil, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.simple_server import make_server

message = ""
def sys_monitor(environ, start_response):
	global message
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	#get boot time
	boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	#get CPU utilization info
	cpu_util = psutil.cpu_percent(interval=1, percpu=True)
	cpu_count = psutil.cpu_count()
	
	#get memory info
	mem = psutil.virtual_memory()
	
	#set the threshold of memory usage to 50%
	THRESHOLD = 50
	
	#get disk utilization info
	disk = psutil.disk_usage('/')
	
	#generating html
	#Boot time
	message += "<h1>System Monitor</h1>"
	message += "<table style='background-repeat:no-repeat; width:auto; margin:0;' cellpadding='5' cellspacing='0' border='1'>"
	message += "<tr><th bgcolor='aquamarine' align = 'left'>BOOT TIME</th><td bgcolor='aquamarine' colspan ='2'>" + str(boot_time) + "</td></tr>"
	#CPU
	message += "<tr><th bgcolor='hotpink' align = 'left' rowspan='" + str(cpu_count + 2) + "'>CPU UTILIZATION</th></tr>"
	j = 1
	for cpu in cpu_util:
		message += "<tr><td bgcolor='hotpink'>CPU " + str(j) + "</td><td bgcolor='hotpink'>" + str(cpu) + "%</td><tr>"
		j += 1
	#memory
	message += "<tr><th bgcolor='darkturquoise' align = 'left'>AVAILABLE MEMORY</th><td bgcolor='darkturquoise' colspan ='2'>" + str(mem.available) + "</td></tr>"
	message += "<tr><th bgcolor='darkturquoise' align = 'left'>USED MEMORY</th><td bgcolor='darkturquoise' colspan ='2'>" + str(mem.used) + "</td></tr>"
	message += "<tr><th bgcolor='darkturquoise' align = 'left'>USED MEMORY PERCENTAGE</th><td bgcolor='darkturquoise' colspan ='2'>" + str(mem.percent) + "%</td></tr>"
	#if memory usage is beyond the threshold, output alert message
	if (mem.percent > THRESHOLD):
		message += "<tr><th bgcolor='tomato' align = 'left'>Alert</th><td colspan ='2' bgcolor='tomato'>MEMORY USAGE BEYOND THRESHOLD!</td></tr>"
	#disk
	message += "<tr><th bgcolor='mediumaquamarine' align = 'left'>TOTAL DISK</th><td bgcolor='mediumaquamarine' colspan ='2'>" + str(disk.total) + "</td></tr>"
	message += "<tr><th bgcolor='mediumaquamarine' align = 'left'>USED DISK</th><td bgcolor='mediumaquamarine' colspan ='2'>" + str(disk.used) + "</td></tr>"
	message += "<tr><th bgcolor='mediumaquamarine' align = 'left'>USED DISK PERCENTAGE</th><td bgcolor='mediumaquamarine' colspan ='2'>" + str(disk.percent) + "%</td></tr>"
	message += "</table>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, sys_monitor)
print("Serving on port 8000...")

httpd.serve_forever()



