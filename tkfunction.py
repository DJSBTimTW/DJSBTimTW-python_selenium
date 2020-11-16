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


