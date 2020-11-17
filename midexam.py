import sqlite3,csv,datetime
import tkinter as tk
import tkfunction as tf
from tkinter import ttk
import tkinter.messagebox
from functools import partial

conn = sqlite3.connect('9A517012.db')
try:
    conn.execute('''
        create table if not exists admin
        (
            role char(8)               not null,
            acc  char(8) primary key   not null,
            pwd  char(8)               not null
        );
    ''')
except Exception as e:
    print("資料庫連接或資料表建立失敗")
    exit()

try:
    with open('accounts.csv') as f:
        myCsv = csv.reader(f)
        headers = next(myCsv)
        for row in myCsv:
            conn.execute("insert into admin(role, acc, pwd) select ?,?,? where not exists(select 1 from admin where role=? and acc=?);",(str(row[0]).strip(),str(row[1]).strip(),str(row[2]).strip(),str(row[0]).strip(),str(row[1]).strip()))
            conn.commit()
            cn = conn.total_changes
            if cn == 0:
                print("新增帳號 {} 失敗".format(row[1]))
            else:
                print("新增帳號 {} 成功".format(row[1]))
        conn.close()
except OSError as e:
    print('讀取失敗')
    exit()

class Application(tk.Tk):
    global loginrole,loginacc
    loginrole = "login"
    def __init__(self):
        super().__init__()

        self.wm_title("個人健康資訊工具")
        self.geometry('600x400+50+100')
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (loginpage, adminpage, userpage, bmipage, bestwepage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(loginpage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if loginrole == "login":
            menubar = tk.Menu(self)
            self.configure(menu=menubar)
        elif loginrole == "admin":
            menubar = tk.Menu(self)
            menubar.add_command(label="1.BMI計算",command=lambda: self.showbmipage(0))
            menubar.add_command(label="2.最佳體重計算",command=lambda: self.showbestwepage(0))
            menubar.add_command(label="3.觀看log",command=lambda: self.showlogpage(0))
            menubar.add_command(label="4.離開",command=lambda: self.acclogout(0))
            self.configure(menu=menubar)
        elif loginrole == "user":
            menubar = tk.Menu(self)
            menubar.add_command(label="1.BMI計算",command=lambda: self.showbmipage(0))
            menubar.add_command(label="2.最佳體重計算",command=lambda: self.showbestwepage(0))
            menubar.add_command(label="3.離開",command=lambda: self.acclogout(0))
            self.configure(menu=menubar)
        # menubar = frame.menubar(self)
        # self.configure(menu=menubar)


    def acclogin(self, name,pwd):
        global loginrole,loginacc
        strname = tf.getentry(name)
        strpwd = tf.getentry(pwd)
        lre = tf.login(strname,strpwd)
        if lre == "admin":
            tkinter.messagebox.showinfo('提示','登入成功')
            loginacc = strname
            loginrole = lre
            self.show_frame(adminpage)
            tf.entryclear(name)
            tf.entryclear(pwd)
            print(loginacc)
        elif lre == "user":
            tkinter.messagebox.showinfo('提示','登入成功')
            loginacc = strname
            loginrole = lre
            self.show_frame(userpage)
            tf.entryclear(name)
            tf.entryclear(pwd)
            print(loginacc)
        elif lre == "accno":
            tkinter.messagebox.showerror('提示','帳號錯誤')
            tf.entryclear(name)
            tf.entryclear(pwd)
        elif lre == "pwdno":
            tkinter.messagebox.showerror('提示','密碼錯誤')
            tf.entryclear(pwd)

    def acclogout(self,n):
        print("logout")
        global loginrole,loginacc
        loginrole = "login"
        loginacc = ""
        self.show_frame(loginpage)

    def bmicou(self,he,we):
        hei = tf.getentry(he)
        wei = tf.getentry(we)
        if hei !="" or wei !="":
            bmi = tf.bmicount(hei,wei)
            tkinter.messagebox.showinfo('計算結果','BMI為:{}'.format(bmi))
            tf.twoclear(he,we)
        else:
            tkinter.messagebox.showerror('提示','輸入錯誤')
            tf.twoclear(he,we)

    def bestwe(self,he):
        hei = tf.getentry(he)
        if hei !="":
            we = tf.wecount(hei)
            tkinter.messagebox.showinfo('計算結果','最佳體重為:{}'.format(we))
            tf.entryclear(he)
        else:
            tkinter.messagebox.showerror('提示','輸入錯誤')
            tf.entryclear(he)

    def showbmipage(self,n):
        self.show_frame(bmipage)

    def showbestwepage(self,n):
        self.show_frame(bestwepage)

    def showlogpage(self,n):
        self.show_frame(logpage)

class loginpage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltop = tk.Label(self, text='登入').grid(row='0',column='1',columnspan=3)
        entry1 = tk.Entry(self, show=None)
        entry2 = tk.Entry(self, show='*')
        label1 = tk.Label(self, text="帳號:").grid(row='1',column='0',pady=20)
        label2 = tk.Label(self, text="密碼:").grid(row='2',column='0',pady=20)
        entry1.grid(row='1',column='1',columnspan=3,pady=20)
        entry2.grid(row='2',column='1',columnspan=3,pady=20)

        btnsub = tk.Button(self, text='確定',command=partial(root.acclogin,entry1,entry2))
        btncle = tk.Button(self, text='清除',command=partial(tf.twoclear,entry1,entry2))
        btnsub.grid(row='3',column='1',sticky=tk.E,pady=20)
        btncle.grid(row='3',column='2',sticky=tk.E,pady=20)

class userpage(tk.Frame):
    # user
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="user")
        label.pack(pady=10,padx=10)

class adminpage(tk.Frame):
    # admin
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="admin")
        label.pack(pady=10,padx=10)

class bmipage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltop = tk.Label(self, text='BMI計算(身高以公尺為單位)').grid(row='0',column='1',columnspan=3)
        entry1 = tk.Entry(self, show=None)
        entry2 = tk.Entry(self, show=None)
        label1 = tk.Label(self, text="身高:").grid(row='1',column='0',pady=20)
        label2 = tk.Label(self, text="體重:").grid(row='2',column='0',pady=20)
        entry1.grid(row='1',column='1',columnspan=3,pady=20)
        entry2.grid(row='2',column='1',columnspan=3,pady=20)

        btnsub = tk.Button(self, text='確定',command=lambda: root.bmicou(entry1,entry2))
        btncle = tk.Button(self, text='清除',command=partial(tf.twoclear,entry1,entry2))
        btnsub.grid(row='3',column='1',sticky=tk.E,pady=20)
        btncle.grid(row='3',column='2',sticky=tk.E,pady=20)

class bestwepage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltop = tk.Label(self, text='最佳體重計算(身高以公尺為單位)').grid(row='0',column='1',columnspan=3)
        entry1 = tk.Entry(self, show=None)
        label1 = tk.Label(self, text="身高:").grid(row='1',column='0',pady=20)
        entry1.grid(row='1',column='1',columnspan=3,pady=20)

        btnsub = tk.Button(self, text='確定',command=lambda: root.bestwe(entry1))
        btncle = tk.Button(self, text='清除',command=partial(tf.entryclear,entry1))
        btnsub.grid(row='2',column='1',sticky=tk.E,pady=20)
        btncle.grid(row='2',column='2',sticky=tk.E,pady=20)

class logpage(tk.Frame):
    # admin
    def __init__(self, parent, root):
        super().__init__(parent)


if __name__ == '__main__':
    app = Application()
    app.mainloop()

