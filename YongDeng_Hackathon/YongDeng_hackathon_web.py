from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/show/<username>', methods = ['GET'])
def show_progress(username):
	message = ""
	conn = sqlite3.connect('game.sqlite')
	cursor = conn.cursor()
	try:
		progress = cursor.execute("select * from kid_game where username = ?", (username,)).fetchall()
		percent = int(progress[0][2] / progress[0][1] * 100)
		conn.commit()
		
		message += "<html><head><style><html{display:table;margin:auto;}body{padding-top:50px;margin:20px auto 0 auto;width:60%;font-family:sans-serif;display:table;vertical-align:middle;}"
		message += "table{font-size:24px; width:600px; margin-top:0;} h1{margin:0px;}table{margin:0 auto;}</style></head>"
		message += "<body><h1>Below is the summary of the your kid's progress:</h1>"
		message += "<table cellpadding='15' cellspacing='0' border='2'>"
		message += "<tr><th bgcolor='aquamarine' align = 'left'>Total# of games</th><td bgcolor='aquamarine'>" + str(progress[0][1]) + "</td></tr><br>"
		message += "<tr><th bgcolor='darkturquoise' align = 'left'># of Corrections</th><td bgcolor='darkturquoise'>" + str(progress[0][2]) + "</td></tr><br>"
		message += "<tr><th bgcolor='lime' align = 'left'>Percent Correction</th><td bgcolor='lime'>" + str(percent) + "%</td></tr><br>"
		if (percent < 50):
			message += "<tr><th bgcolor='tomato' align = 'left'>Alert!</th><td bgcolor='tomato'>Your kid could be better!</td></tr><br></table>"
		message += "</body></html>"
		return message
	except Exception as e:
		print(e)
		return 'hello world!'
	finally:
		conn.close()

if __name__ == '__main__':
  app.run( 
        host="localhost",
        port=int("8000"),
        debug=True
  )