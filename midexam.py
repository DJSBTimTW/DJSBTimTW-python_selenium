import sqlite3,csv
import tkinter as tk
import tkfunction as tf
from tkinter import ttk
from datetime import datetime
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
    conn.execute('''
        create table if not exists log
        (
            datetime DATETIME             not null,
            acc  char(8)                  not null,
            action  char(10)               not null
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
    global loginrole,loginacc,showtree
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
        for F in (loginpage, adminpage, userpage, bmipage, bestwepage, logpage):
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
            menubar.add_command(label="3.觀看log",command=lambda: self.showlogpage(1))
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
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            print("{},{},{}".format(dt,loginacc,"登入"))
            tf.loging(dt,loginacc,"登入")
        elif lre == "user":
            tkinter.messagebox.showinfo('提示','登入成功')
            loginacc = strname
            loginrole = lre
            self.show_frame(userpage)
            tf.entryclear(name)
            tf.entryclear(pwd)
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            print("{},{},{}".format(dt,loginacc,"登入"))
            tf.loging(dt,loginacc,"登入")
        elif lre == "accno":
            tkinter.messagebox.showerror('提示','帳號錯誤')
            tf.entryclear(name)
            tf.entryclear(pwd)
        elif lre == "pwdno":
            tkinter.messagebox.showerror('提示','密碼錯誤')
            tf.entryclear(pwd)

    def acclogout(self,n):
        global loginrole,loginacc
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print("{},{},{}".format(dt,loginacc,"離開"))
        tf.loging(dt,loginacc,"離開")
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
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print("{},{},{}".format(dt,loginacc,"BMI計算"))
        tf.loging(dt,loginacc,"BMI計算")

    def showbestwepage(self,n):
        self.show_frame(bestwepage)
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print("{},{},{}".format(dt,loginacc,"最佳體重計算"))
        tf.loging(dt,loginacc,"最佳體重計算")

    def showlogpage(self,n):
        self.show_frame(logpage)
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print("{},{},{}".format(dt,loginacc,"觀看log"))
        tf.loging(dt,loginacc,"觀看log")

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


class adminpage(tk.Frame):
    # admin
    def __init__(self, parent, root):
        super().__init__(parent)


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
        conn = sqlite3.connect('9A517012.db')
        tree = ttk.Treeview(self, columns=('d1', 'd2', 'd3'), show="headings")
        ysb=tkinter.ttk.Scrollbar(self,orient="vertical",command=tree.yview())
        tree.column('d1',width=60,anchor='center')
        tree.heading('d1',text='時間')
        tree.column('d2',width=60,anchor='center')
        tree.heading('d2',text='帳號')
        tree.column('d3',width=60,anchor='center')
        tree.heading('d3',text='動作')
        cursor = conn.execute("select * from log ORDER BY datetime DESC LIMIT 20;")
        for r in cursor:
            tree.insert("",tk.END, values=(r[0], r[1], r[2]))
        conn.close()
        ysb.configure(command=tree.yview)
        tree.configure(yscrollcommand=ysb.set)
        tree.grid()




if __name__ == '__main__':
    app = Application()
    app.mainloop()

