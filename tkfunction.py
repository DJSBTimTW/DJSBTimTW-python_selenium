import sqlite3
import tkinter as tk
import tkinter.messagebox
def login(name,pwd):
    conn = sqlite3.connect('9A517012.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admin WHERE acc=? ',(name,))
    if cursor.fetchone() is not None:
        cursor.execute('SELECT * FROM admin WHERE acc=? AND pwd=? ',(name,pwd))
        if cursor.fetchone() is not None:
            cursor.execute('SELECT * FROM admin WHERE acc=? AND pwd=? ',(name,pwd))
            row=cursor.fetchone()
            if row[0] == "admin":
                return "admin"
            elif row[0] == "user":
                return "user"
        else:
            return "pwdno"
    else:
        return "accno"

def entryclear(e):
    e.delete(0,'end')

def twoclear(e1,e2):
    e1.delete(0,'end')
    e2.delete(0,'end')

# def loging(acc,action):

def bmicount(height,weight):
    height = float(height)
    weight = float(weight)
    bmi = (weight/(height*height))
    return bmi

def wecount(height):
    height = float(height)
    weight = (int(22)*(height*height))
    return weight

def getentry(e):
    o = str(e.get()).strip()
    return o


