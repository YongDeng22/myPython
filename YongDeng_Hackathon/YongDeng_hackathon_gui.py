from tkinter import *
from flask import Flask
import sqlite3
import tkinter
from random import randint

def play():
	global total_games
	global result, score
	global conn
	global cursor

	answer = int(e1.get())
	e1.delete(0, END)

	total_games += 1
	if result == answer:
		score += 1
		l2["text"] = "Correct!"
		# messagebox.showinfo("Correct!")
	else:
		# messagebox.showinfo("Your answer is incorrect!")
		l2["text"] = "Your answer is incorrect!"
	cursor.execute("update kid_game set total_game_count = :total, score =:cscore where username =:username", \
		{"total":total_games, "cscore":score, "username": user_name})
	conn.commit()
		# conn.close()
	b1["command"] = play_again
	b1["text"] = "Play again?"
	e1.pack_forget()
	l1.pack_forget()
	b1.pack
	l2.pack()
	base.mainloop()

def check_user(name, user_list):
	for u in user_list:
		if u[0] == name:
			return True;
	return False

def play_again():
	global user_name
	global l1, e1, l2
	global conn, cursor
	global total_games, score
	# user_name = e1.get()
	e1.delete(0, END)
	user = cursor.execute("select * from kid_game where username =?", (user_name,)).fetchall()

	if (not check_user(user_name, user)):
		cursor.execute("insert into kid_game values(?,?,?)", (user_name,total_games,score))
	else:
		total_games = user[0][1]
		score = user[0][2]

	conn.commit()
	# conn.close()
	operations = ['+', '-', '*', '/']
	b = randint(1,20)
	a = randint(1,20) * b
	op = operations[randint(0, 3)]
	global result
	if op == '+':
		result = a + b
	elif op == '-':
		result = a - b
	elif op == '*':
		result = a * b
	elif op == '/':
		result = a // b

	l1["text"] = str(a) + op + str(b) + "="
	l1.pack( side = LEFT)
	e1.pack(side = LEFT)
	l2.pack()

	b1["text"] = "Submit"
	b1["command"] = play
	b1.pack()
	base.mainloop()



def play_view():
	global user_name
	global l1, e1, l2
	global conn, cursor
	global total_games, score, result
	user_name = e1.get()
	e1.delete(0, END)
	# messagebox.showinfo("Welcome", e1.get())
	user = cursor.execute("select * from kid_game where username =?", (user_name,)).fetchall()
	if (not check_user(user_name, user)):
		cursor.execute("insert into kid_game values(?,?,?)", (user_name,total_games,score))
	else:
		total_games = user[0][1]
		score = user[0][2]
		# kid = Kids(user["username"], user["name"], user["total_game_count"], user["score"])
	conn.commit()
	# conn.close()
	operations = ['+', '-', '*', '/']
	b = randint(1,20)
	a = randint(1,20) * b
	op = operations[randint(0, 3)]
	if op == '+':
		result = a + b
	elif op == '-':
		result = a - b
	elif op == '*':
		result = a * b
	elif op == '/':
		result = a // b

	l1["text"] = str(a) + " " + op + " " + str(b) + "="
	l1.pack( side = LEFT)
	e1.pack(side = LEFT)
	l2.pack()

	b1["text"] = "submit"
	b1["command"] = play
	b1.pack()
	base.mainloop()


conn = sqlite3.connect("game.sqlite")
cursor = conn.cursor()
result = 0
user_name=""
total_games = 0	
score = 0

base = Tk()
base.configure(bg='white')
base.geometry("400x400")
# base.minsize(300, 300)
base.maxsize(1000, 1000)
frame = tkinter.Frame(base)
frame.pack()

l1 = Label(frame, text="User Name", foreground="#696969", font = "Helvetica 16 bold")
l1.pack( side = LEFT, pady = 20)
e1 = Entry(frame)
e1.pack(side = LEFT, pady = 10)

b1 = Button(base, text="Enter", command=play_view, fg="#696969", font = "Helvetica 16 bold")
b1.pack()
l2 = Label(base, text="Let's play!", foreground="#696969", font = "Helvetica 16 bold")
l2.pack(pady = 10)
base.mainloop()
