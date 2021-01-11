import musicbs4,sqlcon,userinfo,appbs4_th,os,sqlite3
import tkinter as tk
from tkinter import ttk,messagebox,StringVar
from PIL import ImageTk, Image
from functools import partial

def showimage(root):
    load = Image.open('gc2b.png')
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render,bg='black',fg='white')
    img.image = render
    img.place(x=99, y=0)
    verinfo = tk.Label(root, text='Ver:1.0',bg='black',fg='white')
    verinfo.place(x=5, y=380, width=40, height=21)

def showmainpageF():
    mainF.place(x=0, y=0, width=300, height=400)
    showimage(mainF)
    btn101 = tk.Button(mainF, text='顯示資料', command=lambda: showpage(),bg='black',fg='white')
    btn101.place(x=75, y=100, width=150, height=25)
    btn102 = tk.Button(mainF, text='抓取資料', command=lambda: showdatapage(),bg='black',fg='white')
    btn102.place(x=75, y=175, width=150, height=25)
    btn103 = tk.Button(mainF, text='修改資料', command=lambda: showmoddatapage(),bg='black',fg='white')
    btn103.place(x=75, y=250, width=150, height=25)
    btn104 = tk.Button(mainF, text='退出', command=lambda: Close(),bg='black',fg='white')
    btn104.place(x=75, y=325, width=150, height=25)

def re_placeF(root):
    frames=['mainF','dataF','showF','userinfoF','playdataF','getmusicF','urlmusicF','manualmusicF','moddataF','modplaydataF','modmusicdataF','modmusicF','showpageF','showinfopageF','showmusicpageF','showplaypageF']
    for i in frames:
        if i!=root:
            eval(i+".place_forget()")

def showmainpage():
    re_placeF('mainF')
    mainF.place(x=0, y=0, width=300, height=400)
    showimage(mainF)
    btn101 = tk.Button(mainF, text='顯示資料', command=lambda: showpage(),bg='black',fg='white')
    btn101.place(x=75, y=100, width=150, height=25)
    btn102 = tk.Button(mainF, text='抓取資料', command=lambda: showdatapage(),bg='black',fg='white')
    btn102.place(x=75, y=175, width=150, height=25)
    btn103 = tk.Button(mainF, text='修改資料', command=lambda: showmoddatapage(),bg='black',fg='white')
    btn103.place(x=75, y=250, width=150, height=25)
    btn104 = tk.Button(mainF, text='退出', command=lambda: Close(),bg='black',fg='white')
    btn104.place(x=75, y=325, width=150, height=25)

def showdatapage():
    re_placeF('dataF')
    dataF.place(x=0, y=0, width=300, height=400)
    showimage(dataF)
    btn201 = tk.Button(dataF, text='抓取玩家資料', command=lambda: showuserinfopage(),bg='black',fg='white')
    btn201.place(x=75, y=100, width=150, height=25)
    btn202 = tk.Button(dataF, text='抓取玩家遊玩資料', command=lambda: showplaydatapage(),bg='black',fg='white')
    btn202.place(x=75, y=175, width=150, height=25)
    btn203 = tk.Button(dataF, text='抓取歌曲資料', command=lambda: showgetmusicpage(),bg='black',fg='white')
    btn203.place(x=75, y=250, width=150, height=25)
    btn204 = tk.Button(dataF, text='返回至首頁', command=lambda: showmainpage(),bg='black',fg='white')
    btn204.place(x=75, y=325, width=150, height=25)

def showuserinfopage():
    re_placeF('userinfoF')
    userinfoF.place(x=0, y=0, width=300, height=400)
    showimage(userinfoF)
    lbtitle = tk.Label(userinfoF, text='登入',bg='black',fg='white')
    lbtitle.place(x=136, y=103, width=30, height=21)

    lbCID = tk.Label(userinfoF, text='卡號：',bg='black',fg='white')
    lbCID.place(x=40, y=150, width=35, height=25)

    lbPWR = tk.Label(userinfoF, text='密碼：',bg='black',fg='white')
    lbPWR.place(x=40, y=175, width=35, height=25)

    entryCID=StringVar()
    entryPWR=StringVar()
    userinfoF.var = StringVar()
    typeinCID = tk.Entry(userinfoF, show=None,textvariable=entryCID,bg='black',fg='white')
    typeinCID.place(x=75, y=150, width=150, height=25)
    typeinPWR = tk.Entry(userinfoF, show='*',textvariable=entryPWR,bg='black',fg='white')
    typeinPWR.place(x=75, y=175, width=150, height=25)

    lbsave = tk.Label(userinfoF, text='已儲存的卡號',bg='black',fg='white')
    lbsave.place(x=112, y=220, width=78, height=25)

    combo = ttk.Combobox(userinfoF)
    combo.place(x=75, y=250, width=150, height=25)
    combo['values'] = combo_values_input()

    def selectdata(tyCID,tyPWR):
        comboget=combo.get()
        if comboget!='':
            print(comboget.strip()+":"+tyPWR.strip())
            info_return = userinfo.getinfo(comboget.strip(),tyPWR.strip())
            if info_return=='OK':
                tk.messagebox.showinfo('提示','抓取成功')
                showdatapage()
            elif info_return=='error':
                tk.messagebox.showerror('錯誤','登入失敗')
                typeinPWR.delete(0,'end')
        elif comboget=='':
            print(tyCID.strip()+":"+tyPWR.strip())
            info_return = userinfo.getinfo(tyCID.strip(),tyPWR.strip())
            if info_return=='OK':
                tk.messagebox.showinfo('提示','抓取成功')
                showdatapage()
            elif info_return=='error':
                tk.messagebox.showerror('錯誤','登入失敗')
                typeinCID.delete(0,'end')
                typeinPWR.delete(0,'end')

    btnlogin = tk.Button(userinfoF, text='確定', command=lambda: selectdata(typeinCID.get(),typeinPWR.get()),bg='black',fg='white')
    # info_select,combo.get(),typeinCID.get(),typeinPWR.get()
    btnlogin.place(x=45, y=330, width=100, height=25)


    btnback = tk.Button(userinfoF, text='返回', command=lambda: showdatapage(),bg='black',fg='white')
    btnback.place(x=155, y=330, width=100, height=25)

def combo_values_input():
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    query = cur.execute('select cid from info')
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data
    cur.close()
    conn.close()

def combo_playinfo_input(playinfo):
    data = []
    for row in playinfo:
        data.append(row)
    return data

def combo_gentext_input():
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    query = cur.execute('select gentext from gen')
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data
    cur.close()
    conn.close()

def combo_gen_input(gentext):
    conn = sqlite3.connect('userdata.db')
    conr = conn.cursor()
    conr.execute('select gen from gen where gentext=?;',(gentext,))
    gendata = conr.fetchone()
    gen=str(gendata).replace("(","").replace(")","").replace("'","").replace(",","").replace("\n","").strip()
    print(gen)
    cur = conn.cursor()
    query = cur.execute('select name from songinfo where gen=?;',(gen,))
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data
    cur.close()
    conr.close()
    conn.close()

def showplaydatapage():
    re_placeF('playdataF')
    playdataF.place(x=0, y=0, width=300, height=400)
    showimage(playdataF)
    lbtitle = tk.Label(playdataF, text='登入',bg='black',fg='white')
    lbtitle.place(x=136, y=103, width=30, height=21)

    lbCID = tk.Label(playdataF, text='卡號：',bg='black',fg='white')
    lbCID.place(x=40, y=150, width=35, height=25)

    lbPWR = tk.Label(playdataF, text='密碼：',bg='black',fg='white')
    lbPWR.place(x=40, y=175, width=35, height=25)

    entryCID=StringVar()
    entryPWR=StringVar()
    playdataF.var = StringVar()
    typeinCID = tk.Entry(playdataF, show=None,bg='black',fg='white')
    typeinCID.place(x=75, y=150, width=150, height=25)
    typeinPWR = tk.Entry(playdataF, show='*',bg='black',fg='white')
    typeinPWR.place(x=75, y=175, width=150, height=25)

    lbsave = tk.Label(playdataF, text='已儲存的卡號',bg='black',fg='white')
    lbsave.place(x=112, y=220, width=78, height=25)

    combo = ttk.Combobox(playdataF)
    combo.place(x=75, y=250, width=150, height=25)
    combo['values'] = combo_values_input()

    def selectdata(tyCID,tyPWR):
        comboget=combo.get()
        if comboget!='':
            print(comboget.strip()+":"+tyPWR.strip())
            playdata_return = appbs4_th.playdata(comboget.strip(),tyPWR.strip())
            if playdata_return=='OK':
                tk.messagebox.showinfo('提示','抓取成功')
                showdatapage()
            elif playdata_return=='error':
                tk.messagebox.showerror('錯誤','登入失敗')
                typeinPWR.delete(0,'end')
        elif comboget=='':
            print(tyCID.strip()+":"+tyPWR.strip())
            playdata_return = appbs4_th.playdata(tyCID.strip(),tyPWR.strip())
            if playdata_return=='OK':
                tk.messagebox.showinfo('提示','抓取成功')
                showdatapage()
            elif playdata_return=='error':
                tk.messagebox.showerror('錯誤','登入失敗')
                typeinCID.delete(0,'end')
                typeinPWR.delete(0,'end')

    btnlogin = tk.Button(playdataF, text='確定', command=lambda: selectdata(typeinCID.get(),typeinPWR.get()),bg='black',fg='white')
    btnlogin.place(x=45, y=330, width=100, height=25)

    btnback = tk.Button(playdataF, text='返回', command=lambda: showdatapage(),bg='black',fg='white')
    btnback.place(x=155, y=330, width=100, height=25)

def showgetmusicpage():
    re_placeF('getmusicF')
    getmusicF.place(x=0, y=0, width=300, height=400)
    showimage(getmusicF)
    btn301 = tk.Button(getmusicF, text='抓取歌曲資料', command=lambda: getmusicdata(),bg='black',fg='white')
    btn301.place(x=75, y=100, width=150, height=25)
    btn302 = tk.Button(getmusicF, text='輸入URL抓取歌曲資料', command=lambda: showurlmusicpage(),bg='black',fg='white')
    btn302.place(x=75, y=175, width=150, height=25)
    btn303 = tk.Button(getmusicF, text='手動輸入', command=lambda: manualmusicpage(),bg='black',fg='white')
    btn303.place(x=75, y=250, width=150, height=25)
    btn304 = tk.Button(getmusicF, text='返回', command=lambda: showdatapage(),bg='black',fg='white')
    btn304.place(x=75, y=325, width=150, height=25)

def getmusicdata():
    tk.messagebox.showinfo('提示','即將開始抓取資料')
    musicbs4.getmusic()
    tk.messagebox.showinfo('提示','抓取資料結束')
    showdatapage()

def getmusicurldata(ty):
    tk.messagebox.showinfo('提示','即將開始抓取資料')
    musicbs4.getmusicbs4(ty)
    tk.messagebox.showinfo('提示','抓取資料結束')
    showdatapage()

def showurlmusicpage():
    re_placeF('urlmusicF')
    urlmusicF.place(x=0, y=0, width=300, height=400)
    showimage(urlmusicF)
    lburl = tk.Label(urlmusicF, text='輸入URL',bg='black',fg='white')
    lburl.place(x=125, y=103, width=50, height=21)
    typeinURL = tk.Entry(urlmusicF, show=None,bg='black',fg='white')
    typeinURL.place(x=75, y=150, width=150, height=25)
    btnurl = tk.Button(urlmusicF, text='確定', command=lambda: getmusicurldata(typeinURL.get()),bg='black',fg='white')
    btnurl.place(x=45, y=330, width=100, height=25)

    btnback = tk.Button(urlmusicF, text='返回', command=lambda: showgetmusicpage(),bg='black',fg='white')
    btnback.place(x=155, y=330, width=100, height=25)

def manualmusicpage():
    re_placeF('manualmusicF')
    manualmusicF.place(x=0, y=0, width=300, height=400)
    showimage(manualmusicF)
    lbma = tk.Label(manualmusicF, text='輸入歌曲資料(無EX難度則留空)',bg='black',fg='white')
    lbma.place(x=65, y=103, width=170, height=21)

    ename_var = StringVar()
    earts_var = StringVar()
    ebpm_var = StringVar()
    egen_var = StringVar()
    eslv_var = StringVar()
    enlv_var = StringVar()
    ehlv_var = StringVar()
    eelv_var = StringVar()
    manualmusicF.var = StringVar()
    # songinfo={'name': name, 'arts': arts, 'bpm': bpm, 'gen': gen, 'simple': sslv, 'normal': snlv, 'hard': shlv, 'extra': selv, 'del': '0'}
    ename = tk.Entry(manualmusicF,textvariable=ename_var,bg='black',fg='white')
    ename.place(x=75, y=130, width=150, height=25)
    earts = tk.Entry(manualmusicF,textvariable=earts_var,bg='black',fg='white')
    earts.place(x=75, y=155, width=150, height=25)
    ebpm = tk.Entry(manualmusicF,textvariable=ebpm_var,bg='black',fg='white')
    ebpm.place(x=75, y=180, width=150, height=25)
    egen = tk.Entry(manualmusicF,textvariable=egen_var,bg='black',fg='white')
    egen.place(x=75, y=205, width=150, height=25)
    eslv = tk.Entry(manualmusicF,textvariable=eslv_var,bg='black',fg='white')
    eslv.place(x=75, y=230, width=150, height=25)
    enlv = tk.Entry(manualmusicF,textvariable=enlv_var,bg='black',fg='white')
    enlv.place(x=75, y=255, width=150, height=25)
    ehlv = tk.Entry(manualmusicF,textvariable=ehlv_var,bg='black',fg='white')
    ehlv.place(x=75, y=280, width=150, height=25)
    eelv = tk.Entry(manualmusicF,textvariable=eelv_var,bg='black',fg='white')
    eelv.place(x=75, y=305, width=150, height=25)

    lbname = tk.Label(manualmusicF, text='歌名:',bg='black',fg='white').place(x=35, y=130, width=35, height=25)
    lbarts = tk.Label(manualmusicF, text='作者:',bg='black',fg='white').place(x=35, y=155, width=35, height=25)
    lbbpm = tk.Label(manualmusicF, text='速度:',bg='black',fg='white').place(x=35, y=180, width=35, height=25)
    lbgen = tk.Label(manualmusicF, text='分類:',bg='black',fg='white').place(x=35, y=205, width=35, height=25)
    lbslv = tk.Label(manualmusicF, text='簡單難度:',bg='black',fg='white').place(x=10, y=230, width=60, height=25)
    lbnlv = tk.Label(manualmusicF, text='普通難度:',bg='black',fg='white').place(x=10, y=255, width=60, height=25)
    lbhlv = tk.Label(manualmusicF, text='困難難度:',bg='black',fg='white').place(x=10, y=280, width=60, height=25)
    lbelv = tk.Label(manualmusicF, text='EX難度:',bg='black',fg='white').place(x=20, y=305, width=50, height=25)

    def select_data(ename,earts,ebpm,egen,eslv,enlv,ehlv,eelv):
        if (ename!='' and earts!='' and ebpm!='' and egen!='' and eslv!='' and enlv!='' and ehlv!=''):
            if eelv!='':
                songinfo={'name': ename.strip(), 'arts': earts.strip(), 'bpm': ebpm.strip(), 'gen': egen.strip(), 'simple': eslv.strip(), 'normal': enlv.strip(), 'hard': ehlv.strip(), 'extra': eelv.strip(), 'del': '0'}
                re = musicbs4.manualmusic(songinfo)
                if re == 'OK':
                    tk.messagebox.showinfo('提示','歌曲:{}新增成功'.format(ename.strip()))
                    showdatapage()
                elif re == 'dberror':
                    tk.messagebox.showerror('錯誤','資料庫連接失敗')
                elif re == 'daerror':
                    tk.messagebox.showerror('錯誤','新增失敗')
            else:
                songinfo={'name': ename.strip(), 'arts': earts.strip(), 'bpm': ebpm.strip(), 'gen': egen.strip(), 'simple': eslv.strip(), 'normal': enlv.strip(), 'hard': ehlv.strip(), 'extra': '0', 'del': '0'}
                re = musicbs4.manualmusic(songinfo)
                if re == 'OK':
                    tk.messagebox.showinfo('提示','歌曲:{}新增成功'.format(ename.strip()))
                    showdatapage()
                elif re == 'dberror':
                    tk.messagebox.showerror('錯誤','資料庫連接失敗')
                elif re == 'daerror':
                    tk.messagebox.showerror('錯誤','新增失敗')
        else:
            tk.messagebox.showerror('錯誤','ex難度以外的值不能為空')
            manualmusicpage()

    btnurl = tk.Button(manualmusicF, text='確定', command=lambda: select_data(ename.get(),earts.get(),ebpm.get(),egen.get(),eslv.get(),enlv.get(),ehlv.get(),eelv.get()),bg='black',fg='white')
    btnurl.place(x=45, y=350, width=100, height=25)

    btnback = tk.Button(manualmusicF, text='返回', command=lambda: showdatapage(),bg='black',fg='white')
    btnback.place(x=155, y=350, width=100, height=25)

def showmoddatapage():
    re_placeF('moddataF')
    moddataF.place(x=0, y=0, width=300, height=400)
    showimage(moddataF)
    btn101 = tk.Button(moddataF, text='玩家資料', command=lambda: modplaydatapage(),bg='black',fg='white')
    btn101.place(x=75, y=100, width=150, height=25)
    btn102 = tk.Button(moddataF, text='歌曲資料', command=lambda: modmusicdatapage(),bg='black',fg='white')
    btn102.place(x=75, y=175, width=150, height=25)
    btnback = tk.Button(moddataF, text='返回至首頁', command=lambda: showmainpage(),bg='black',fg='white')
    btnback.place(x=75, y=325, width=150, height=25)

def modplaydatapage():
    re_placeF('modplaydataF')
    modplaydataF.place(x=0, y=0, width=300, height=400)
    showimage(modplaydataF)
    lb101 = tk.Label(modplaydataF, text='選擇卡號刪除資料',bg='black',fg='white')
    lb101.place(x=75, y=100, width=150, height=25)
    lbCID = tk.Label(modplaydataF, text='卡號：',bg='black',fg='white')
    lbCID.place(x=40, y=125, width=35, height=25)

    modplaydataF.var = StringVar()
    combo = ttk.Combobox(modplaydataF)
    combo.place(x=75, y=125, width=150, height=25)
    combo['values'] = combo_values_input()

    def delete_info():
        comboget=combo.get()
        if comboget!='':
            ask=tk.messagebox.askyesno('提示', '要執行此操作嗎')
            if ask is True:
                ret=sqlcon.deleteinfo(comboget)
                if ret=='OK':
                    tk.messagebox.showinfo('提示','刪除成功')
                    modplaydatapage()
                elif ret=='error':
                    tk.messagebox.showerror('錯誤','刪除失敗')
                    modplaydatapage()
            else:
                modplaydatapage()
        else:
            tk.messagebox.showerror('錯誤','請選擇卡號')
            modplaydatapage()

    def delete_pld():
        comboget=combo.get()
        if comboget!='':
            ask=tk.messagebox.askyesno('提示', '要執行此操作嗎')
            if ask is True:
                ret=sqlcon.deletepld(comboget)
                if ret=='OK':
                    tk.messagebox.showinfo('提示','刪除成功')
                    modplaydatapage()
                elif ret=='error':
                    tk.messagebox.showerror('錯誤','刪除失敗')
                    modplaydatapage()
            else:
                modplaydatapage()
        else:
            tk.messagebox.showerror('錯誤','請選擇卡號')
            modplaydatapage()

    btninfo = tk.Button(modplaydataF, text='刪除玩家資料', command=lambda: delete_info(),bg='black',fg='white')
    btninfo.place(x=75, y=175, width=150, height=25)
    btnpld = tk.Button(modplaydataF, text='刪除遊玩資料資料', command=lambda: delete_pld(),bg='black',fg='white')
    btnpld.place(x=75, y=250, width=150, height=25)

    btnback = tk.Button(modplaydataF, text='返回', command=lambda: showmoddatapage(),bg='black',fg='white')
    btnback.place(x=75, y=325, width=150, height=25)

def modmusicdatapage():
    mainF.place_forget()

    dataF.place_forget()

    showF.place_forget()

    userinfoF.place_forget()

    playdataF.place_forget()

    getmusicF.place_forget()

    urlmusicF.place_forget()

    manualmusicF.place_forget()

    moddataF.place_forget()

    modplaydataF.place_forget()

    modmusicF.place_forget()

    showpageF.place_forget()

    showinfopageF.place_forget()

    showmusicpageF.place_forget()

    showplaypageF.place_forget()
    modmusicdataF.place(x=0, y=0, width=300, height=400)
    showimage(modmusicdataF)

    modmusicdataF.var = StringVar()
    gencombo = ttk.Combobox(modmusicdataF)
    gencombo.place(x=75, y=100, width=150, height=25)
    gencombo['values'] = combo_gentext_input()
    lbgen = tk.Label(modmusicdataF,text='依分類選擇',bg='black',fg='white').place(x=5, y=100, width=70, height=25)
    musiccombo = ttk.Combobox(modmusicdataF)

    def gentextselect():
        btnen.place(x=45, y=250, width=100, height=25)
        btndl.place(x=155, y=250, width=100, height=25)
        musiccombo.place(x=75, y=175, width=150, height=25)
        musiccombo['values'] = combo_gen_input(gencombo.get())

    def clearcombo():
        gencombo.set('')
        musiccombo.set('')
        musiccombo.place_forget()
        btnen.place_forget()
        btndl.place_forget()

    def backpage():
        clearcombo()
        showmoddatapage()

    def gomodpage(musiccombodata):
        clearcombo()
        modmusic(musiccombodata)

    def deletmusic(musiccombodata):
        ask=tk.messagebox.askyesno('提示', '要執行此操作嗎')
        if ask is True:
            ren=sqlcon.deletemusic(musiccombodata)
            if ren=='OK':
                tk.messagebox.showinfo('提示','刪除成功')
                backpage()
            elif ren=='error':
                tk.messagebox.showerror('錯誤','刪除失敗')
                backpage()
        else:
            clearcombo()

    btnen = tk.Button(modmusicdataF, text='修改', command=lambda: gomodpage(musiccombo.get()),bg='black',fg='white')
    btndl = tk.Button(modmusicdataF, text='刪除', command=lambda: deletmusic(musiccombo.get()),bg='black',fg='white')
    btnclk = tk.Button(modmusicdataF, text='刷新', command=lambda: gentextselect(),bg='black',fg='white')
    btnclk.place(x=45, y=350, width=100, height=25)
    btnback = tk.Button(modmusicdataF, text='返回', command=lambda: backpage(),bg='black',fg='white')
    btnback.place(x=155, y=350, width=100, height=25)

def modmusic(musiccombo):
    mainF.place_forget()

    dataF.place_forget()

    showF.place_forget()

    userinfoF.place_forget()

    playdataF.place_forget()

    getmusicF.place_forget()

    urlmusicF.place_forget()

    manualmusicF.place_forget()

    moddataF.place_forget()

    modplaydataF.place_forget()

    modmusicdataF.place_forget()

    showpageF.place_forget()

    showinfopageF.place_forget()

    showmusicpageF.place_forget()

    showplaypageF.place_forget()
    modmusicF.place(x=0, y=0, width=300, height=400)
    showimage(modmusicF)
    data = sqlcon.selectmusic(musiccombo)

    ename_var = StringVar()
    earts_var = StringVar()
    ebpm_var = StringVar()
    egen_var = StringVar()
    eslv_var = StringVar()
    enlv_var = StringVar()
    ehlv_var = StringVar()
    eelv_var = StringVar()
    delvar_var = StringVar()
    manualmusicF.var = StringVar()
    # songinfo={'name': name, 'arts': arts, 'bpm': bpm, 'gen': gen, 'simple': sslv, 'normal': snlv, 'hard': shlv, 'extra': selv, 'del': '0'}
    ename = tk.Label(modmusicF,text=data[0],bg='black',fg='white')
    ename.place(x=75, y=130, width=150, height=25)

    earts = tk.Entry(modmusicF,textvariable=earts_var,bg='black',fg='white')
    earts.insert(0,data[1])
    earts.place(x=75, y=155, width=150, height=25)

    ebpm = tk.Entry(modmusicF,textvariable=ebpm_var,bg='black',fg='white')
    ebpm.insert(0,data[2])
    ebpm.place(x=75, y=180, width=150, height=25)

    egen = tk.Entry(modmusicF,textvariable=egen_var,bg='black',fg='white')
    egen.insert(0,data[3])
    egen.place(x=75, y=205, width=150, height=25)

    eslv = tk.Entry(modmusicF,textvariable=eslv_var,bg='black',fg='white')
    eslv.insert(0,data[4])
    eslv.place(x=75, y=230, width=150, height=25)

    enlv = tk.Entry(modmusicF,textvariable=enlv_var,bg='black',fg='white')
    enlv.insert(0,data[5])
    enlv.place(x=75, y=255, width=150, height=25)

    ehlv = tk.Entry(modmusicF,textvariable=ehlv_var,bg='black',fg='white')
    ehlv.insert(0,data[6])
    ehlv.place(x=75, y=280, width=150, height=25)

    eelv = tk.Entry(modmusicF,textvariable=eelv_var,bg='black',fg='white')
    eelv.insert(0,data[7])
    eelv.place(x=75, y=305, width=150, height=25)

    delvar = tk.Entry(modmusicF,textvariable=delvar_var,bg='black',fg='white')
    delvar.insert(0,data[8])
    delvar.place(x=75, y=330, width=150, height=25)

    lbname = tk.Label(modmusicF, text='歌名:',bg='black',fg='white').place(x=35, y=130, width=35, height=25)
    lbarts = tk.Label(modmusicF, text='作者:',bg='black',fg='white').place(x=35, y=155, width=35, height=25)
    lbbpm = tk.Label(modmusicF, text='速度:',bg='black',fg='white').place(x=35, y=180, width=35, height=25)
    lbgen = tk.Label(modmusicF, text='分類:',bg='black',fg='white').place(x=35, y=205, width=35, height=25)
    lbslv = tk.Label(modmusicF, text='簡單難度:',bg='black',fg='white').place(x=10, y=230, width=60, height=25)
    lbnlv = tk.Label(modmusicF, text='普通難度:',bg='black',fg='white').place(x=10, y=255, width=60, height=25)
    lbhlv = tk.Label(modmusicF, text='困難難度:',bg='black',fg='white').place(x=10, y=280, width=60, height=25)
    lbelv = tk.Label(modmusicF, text='EX難度:',bg='black',fg='white').place(x=20, y=305, width=50, height=25)
    lbdel = tk.Label(modmusicF, text='是否刪除:',bg='black',fg='white').place(x=10, y=330, width=60, height=25)

    def updatemusicdata(nname):
        ask=tk.messagebox.askyesno('提示', '要執行此操作嗎')
        if ask is True:
            newdata=[nname,earts.get(),ebpm.get(),egen.get(),eslv.get(),enlv.get(),ehlv.get(),eelv.get(),delvar.get()]
            ren=sqlcon.upmusic(newdata)
            if ren=='OK':
                tk.messagebox.showinfo('提示','修改成功')
                modmusicdatapage()
            elif ren=='error':
                tk.messagebox.showerror('錯誤','修改失敗')
                modmusicdatapage()
        else:
            modmusicdatapage()

    btnen = tk.Button(modmusicF, text='確定修改', command=lambda: updatemusicdata(data[0]),bg='black',fg='white')
    btnen.place(x=45, y=360, width=100, height=25)
    btnback = tk.Button(modmusicF, text='返回', command=lambda: modmusicdatapage(),bg='black',fg='white')
    btnback.place(x=155, y=360, width=100, height=25)

def showpage():
    re_placeF('showpageF')
    showpageF.place(x=0, y=0, width=300, height=400)
    showimage(showpageF)
    btn101 = tk.Button(showpageF, text='玩家資料', command=lambda: showinfopage(),bg='black',fg='white')
    btn101.place(x=75, y=100, width=150, height=25)
    btn102 = tk.Button(showpageF, text='遊玩資料', command=lambda: showplaypage(),bg='black',fg='white')
    btn102.place(x=75, y=175, width=150, height=25)
    btn103 = tk.Button(showpageF, text='歌曲資料', command=lambda: showmusicpage(),bg='black',fg='white')
    btn103.place(x=75, y=250, width=150, height=25)
    btn104 = tk.Button(showpageF, text='返回至首頁', command=lambda: showmainpage(),bg='black',fg='white')
    btn104.place(x=75, y=325, width=150, height=25)

def showinfopage():
    re_placeF('showinfopageF')
    showinfopageF.place(x=0, y=0, width=300, height=400)
    showimage(showinfopageF)

    lbsave = tk.Label(showinfopageF, text='選擇卡號',bg='black',fg='white')
    lbsave.place(x=75, y=100, width=150, height=25)

    showinfopageF.var = StringVar()
    combo = ttk.Combobox(showinfopageF)
    combo.place(x=75, y=130, width=150, height=25)
    combo['values'] = combo_values_input()

    # lbna = tk.Label(showinfopageF, text='ID:',bg='black',fg='white').place(x=0,y=170,width=40, height=25)
    # lbra = tk.Label(showinfopageF, text='排名:',bg='black',fg='white').place(x=150,y=170,width=40, height=25)
    # lbar = tk.Label(showinfopageF, text='領航員:',bg='black',fg='white').place(x=0,y=210,width=40, height=25)
    # lbti = tk.Label(showinfopageF, text='稱號:',bg='black',fg='white').place(x=0,y=240,width=40, height=25)

    def select_data(combodata):
        if combodata!='':
            ren=sqlcon.showinfo(combodata)
            if ren!='error':
                count3=int(int(ren[17])/3)
                countmon=count3*30
                tk.messagebox.showinfo('資料獲取成功','ID:{}\n排名:{}\n領航員:{}\n稱號:{}\n總遊玩次數:{}次\n大約 {}道 約花費{}元'.format(ren[1],ren[5],ren[6],ren[7],ren[17],count3,countmon))
                showpage()
                # lbna_da = tk.Label(showinfopageF, text=ren[1],bg='black',fg='white').place(x=40,y=170,width=100, height=25)
                # lbra_da = tk.Label(showinfopageF, text=ren[5],bg='black',fg='white').place(x=190,y=170,width=100, height=25)
                # lbar_da = tk.Label(showinfopageF, text=ren[6],bg='black',fg='white').place(x=40,y=210,width=200, height=25)
                # lbti_da = tk.Label(showinfopageF, text=ren[7],bg='black',fg='white').place(x=40,y=240,width=200, height=25)
            elif ren=='error':
                tk.messagebox.showerror('錯誤','獲取失敗')
        elif combodata=='':
            tk.messagebox.showerror('錯誤','值不能為空')

    btnr = tk.Button(showinfopageF,text='確定', command=lambda: select_data(combo.get()),bg='black',fg='white').place(x=75, y=250, width=150, height=25)
    btnback = tk.Button(showinfopageF,text='返回', command=lambda: showpage(),bg='black',fg='white').place(x=75, y=325, width=150, height=25)

def showmusicpage():
    re_placeF('showmusicpageF')
    showmusicpageF.place(x=0, y=0, width=300, height=400)
    showimage(showmusicpageF)
    showmusicpageF.var = StringVar()
    gencombo = ttk.Combobox(showmusicpageF)
    gencombo.place(x=75, y=100, width=150, height=25)
    gencombo['values'] = combo_gentext_input()
    lbgen = tk.Label(showmusicpageF,text='依分類選擇',bg='black',fg='white').place(x=5, y=100, width=70, height=25)
    musiccombo = ttk.Combobox(showmusicpageF)

    def gentextselect():
        btnshow.place(x=75, y=225, width=150, height=25)
        musiccombo.place(x=75, y=175, width=150, height=25)
        musiccombo['values'] = combo_gen_input(gencombo.get())

    def clearcombo():
        gencombo.set('')
        musiccombo.set('')
        musiccombo.place_forget()
        btnshow.place_forget()

    def backpage():
        clearcombo()
        showpage()

    def showdata(musiccombo):
        if musiccombo!='':
            ren=sqlcon.selectmusic(musiccombo)
            if ren!='':
                conn = sqlite3.connect('userdata.db')
                cur = conn.cursor()
                cur.execute('select gentext from gen where gen=?;',(ren[3],))
                gendata = cur.fetchone()
                gen=str(gendata).replace("(","").replace(")","").replace("'","").replace(",","").replace("\n","").strip()
                cur.close()
                conn.close()
                if ren[7]!=0:
                    if  ren[8]=='0':
                        tk.messagebox.showinfo('成功','歌名:{}\n作者:{}\nbpm:{}\n分類:{}\n簡單難度:{}\n普通難度:{}\n困難難度:{}\nEX難度:{}\n是否刪除:{}'.format(ren[0],ren[1],ren[2],gen,ren[4],ren[5],ren[6],ren[7],'否'))
                    elif ren[8]=='1':
                        tk.messagebox.showinfo('成功','歌名:{}\n作者:{}\nbpm:{}\n分類:{}\n簡單難度:{}\n普通難度:{}\n困難難度:{}\nEX難度:{}\n是否刪除:{}'.format(ren[0],ren[1],ren[2],gen,ren[4],ren[5],ren[6],ren[7],'是'))
                elif ren[7]==0:
                    if  ren[8]=='0':
                        tk.messagebox.showinfo('成功','歌名:{}\n作者:{}\nbpm:{}\n分類:{}\n簡單難度:{}\n普通難度:{}\n困難難度:{}\n是否刪除:{}'.format(ren[0],ren[1],ren[2],gen,ren[4],ren[5],ren[6],'否'))
                    elif ren[8]=='1':
                        tk.messagebox.showinfo('成功','歌名:{}\n作者:{}\nbpm:{}\n分類:{}\n簡單難度:{}\n普通難度:{}\n困難難度:{}\n是否刪除:{}'.format(ren[0],ren[1],ren[2],gen,ren[4],ren[5],ren[6],'是'))
            elif ren=='':
                tk.messagebox.showerror('錯誤','獲取失敗')
        else:
            tk.messagebox.showerror('錯誤','請選擇歌曲')

    btnshow = tk.Button(showmusicpageF, text='顯示', command=lambda: showdata(musiccombo.get()),bg='black',fg='white')
    btnclk = tk.Button(showmusicpageF, text='刷新', command=lambda: gentextselect(),bg='black',fg='white')
    btnclk.place(x=45, y=350, width=100, height=25)
    btnback = tk.Button(showmusicpageF, text='返回', command=lambda: backpage(),bg='black',fg='white')
    btnback.place(x=155, y=350, width=100, height=25)

def showplaypage():
    re_placeF('showplaypageF')
    showplaypageF.place(x=0, y=0, width=300, height=400)
    showimage(showplaypageF)

    gentext = StringVar()
    lvtext = StringVar()
    cidtext = StringVar()
    musictext =StringVar()

    lbcid = tk.Label(showplaypageF, text='選擇卡號',bg='black',fg='white')
    lbcid.place(x=75, y=100, width=150, height=25)
    cidcombo = ttk.Combobox(showplaypageF,textvariable=cidtext)
    cidcombo.place(x=75, y=130, width=150, height=25)
    cidcombo['values'] = combo_values_input()

    gencombo = ttk.Combobox(showplaypageF,textvariable=gentext)
    gencombo.place(x=5, y=200, width=140, height=25)
    gencombo['values'] = combo_gentext_input()
    lbgen = tk.Label(showplaypageF,text='選擇分類',bg='black',fg='white').place(x=50, y=170, width=50, height=25)
    lblv = tk.Label(showplaypageF,text='選擇等級',bg='black',fg='white').place(x=200, y=170, width=50, height=25)

    musiccombo = ttk.Combobox(showplaypageF,textvariable=musictext)

    lvcombo = ttk.Combobox(showplaypageF,textvariable=lvtext)
    lvcombo.place(x=155, y=200, width=140, height=25)
    def lvlist():
        data=[]
        for i in range(1,16):
            data.append(i)
        return data
    lvcombo['values'] = lvlist()

    def getinfo():
        musiccombo.set('')
        gente = gencombo.get().strip()
        lvte = lvcombo.get().strip()
        cidte = cidcombo.get().strip()
        if (cidte=='' or gente=='' or lvte==''):
            tk.messagebox.showerror('錯誤','值不能為空')
        else:
            conn = sqlite3.connect('userdata.db')
            cur = conn.cursor()
            cur.execute('select gen from gen where gentext=?;',(gente,))
            gendata = cur.fetchone()
            gen=str(gendata).replace("(","").replace(")","").replace("'","").replace(",","").replace("\n","").strip()
            cur.close()
            conn.close()
            ren=sqlcon.selectplayinfo(cidte,gen,lvte)
            if ren!='error':
                musiccombo.place(x=80, y=250, width=140, height=25)
                musiccombo['values'] = combo_playinfo_input(ren)
                btnen.place(x=80, y=300, width=140, height=25)
            elif ren=='error':
                tk.messagebox.showerror('錯誤','獲取失敗')

    def getdata():
        musicname = musiccombo.get()
        cidte = cidcombo.get().strip()
        if (musicname=='' or cidte==''):
            tk.messagebox.showerror('錯誤','值不能為空')
        else:
            ren = sqlcon.selectplaydata(cidte,musicname)
            if ren!='error':
                if len(ren)==10:
                    info = '歌名:{}\n簡單遊玩次數{}\n簡單遊玩分數{}\n普通遊玩次數{}\n普通遊玩分數{}\n困難遊玩次數{}\n困難遊玩分數{}\nEX遊玩次數{}\nEX遊玩分數{}'.format(ren[1],ren[2],ren[3],ren[4],ren[5],ren[6],ren[7],ren[8],ren[9])
                    tk.messagebox.showinfo('成功','{}'.format(info))
                elif len(ren)==8:
                    info = '歌名:{}\n簡單遊玩次數{}\n簡單遊玩分數{}\n普通遊玩次數{}\n普通遊玩分數{}\n困難遊玩次數{}\n困難遊玩分數{}'.format(ren[1],ren[2],ren[3],ren[4],ren[5],ren[6],ren[7])
                    tk.messagebox.showinfo('成功','{}'.format(info))
            elif ren=='error':
                tk.messagebox.showerror('錯誤','獲取失敗')

    def back():
        cidcombo.set('')
        lvcombo.set('')
        musiccombo.place_forget()
        btnen.place_forget()
        showpage()

    btnen = tk.Button(showplaypageF,command=lambda: getdata(), text='確定',bg='black',fg='white')
    btnclk = tk.Button(showplaypageF,command=lambda: getinfo(), text='刷新',bg='black',fg='white')
    btnclk.place(x=45, y=350, width=100, height=25)
    btnback = tk.Button(showplaypageF, text='返回',command=lambda: back(),bg='black',fg='white')
    btnback.place(x=155, y=350, width=100, height=25)


sqlcon.gendb()
form = tk.Tk()
s=ttk.Style()
s.theme_use('alt')
form.geometry('300x400+50+100')
form.resizable(False, False)
form.title('GC資料抓取')
form.iconphoto(True, tk.PhotoImage(file='newicon.png'))

def Close():
    form.destroy()

mainF = tk.Frame(form,bg='black')
mainF.title="mainF"

dataF = tk.Frame(form,bg='black')
dataF.title="dataF"

showF = tk.Frame(form,bg='black')
showF.title="showF"

userinfoF = tk.Frame(form,bg='black')
userinfoF.title="userinfoF"

playdataF = tk.Frame(form,bg='black')
playdataF.title="playdataF"

getmusicF = tk.Frame(form,bg='black')
getmusicF.title="getmusicF"

urlmusicF = tk.Frame(form,bg='black')
urlmusicF.title="urlmusicF"

manualmusicF = tk.Frame(form,bg='black')
manualmusicF.title="manualmusicF"

moddataF = tk.Frame(form,bg='black')
moddataF.title="moddataF"

modplaydataF = tk.Frame(form,bg='black')
modplaydataF.title="modplaydataF"

modmusicdataF = tk.Frame(form,bg='black')
modmusicdataF.title="modmusicdataF"

modmusicF = tk.Frame(form,bg='black')
modmusicF.title="modmusicF"

showpageF = tk.Frame(form,bg='black')
showpageF.title="showpageF"

showinfopageF = tk.Frame(form,bg='black')
showinfopageF.title="showinfopageF"

showmusicpageF = tk.Frame(form,bg='black')
showmusicpageF.title="showmusicpageF"

showplaypageF = tk.Frame(form,bg='black')
showplaypageF.title="showplaypageF"

showmainpageF()


form.mainloop()