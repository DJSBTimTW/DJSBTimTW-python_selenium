import sqlite3,csv
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
        for F in (loginPage, adminpage, userpage, ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(loginPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        menubar = frame.menubar(self)
        self.configure(menu=menubar)

    def login(self, name,pwd):
        strname = name.get()
        strpwd = pwd.get()
        lre = tf.login(strname,strpwd)
        if lre == "admin":
            tkinter.messagebox.showinfo('提示','登入成功')
            self.show_frame(adminpage)
        elif lre == "user":
            tkinter.messagebox.showinfo('提示','登入成功')
            self.show_frame(userpage)
        elif lre == "accno":
            tkinter.messagebox.showerror('提示','帳號錯誤')
            tf.entryclear(name)
            tf.entryclear(pwd)
        elif lre == "pwdno":
            tkinter.messagebox.showerror('提示','密碼錯誤')
            tf.entryclear(pwd)



class loginPage(tk.Frame):
    '''主页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltop = tk.Label(self, text='登入').grid(row='0',column='1',columnspan=3)
        entry1 = tk.Entry(self, show=None)
        entry2 = tk.Entry(self, show='*')
        label1 = tk.Label(self, text="帳號:").grid(row='1',column='0',pady=20)
        label2 = tk.Label(self, text="帳號:").grid(row='2',column='0',pady=20)
        entry1.grid(row='1',column='1',columnspan=3,pady=20)
        entry2.grid(row='2',column='1',columnspan=3,pady=20)

        btnsub = tk.Button(self, text='確定',command=partial(root.login,entry1,entry2))
        btncle = tk.Button(self, text='清除',command=partial(tf.entryclear,entry1,entry2))
        btnsub.grid(row='3',column='1',sticky=tk.E,pady=20)
        btncle.grid(row='3',column='2',sticky=tk.E,pady=20)

    def menubar(salf, root):
        menubar = tk.Menu(root)
        return menubar



class adminpage(tk.Frame):
    # admin
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="admin")
        label.pack(pady=10,padx=10)

    def menubar(salf, root):
        menubar = tk.Menu(root)
        menubar.add_cascade(label="1.BMI計算")
        menubar.add_cascade(label="2.最佳體重計算")
        menubar.add_cascade(label="3.觀看log")
        menubar.add_cascade(label="4.離開")
        return menubar




class userpage(tk.Frame):
    # user
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="user")
        label.pack(pady=10,padx=10)

    def menubar(salf, root):
        menubar = tk.Menu(root)
        menubar.add_cascade(label="1.BMI計算")
        menubar.add_cascade(label="2.最佳體重計算")
        menubar.add_cascade(label="3.離開")
        return menubar



if __name__ == '__main__':
    app = Application()
    app.mainloop()

