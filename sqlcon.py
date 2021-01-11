import sqlite3

def playdb():
    conn = sqlite3.connect('userdata.db')
    conn.execute('''
        create table if not exists playdata
        (
                cid          char(16)  not null,
                name         text      not null,
                spc          INTEGER   not null,
                sps          INTEGER   not null,
                npc          INTEGER   not null,
                nps          INTEGER   not null,
                hpc          INTEGER   not null,
                hps          INTEGER   not null,
                epc          INTEGER   not null,
                eps          INTEGER   not null,
                primary key (cid,name)
        );
    ''')
    conn.commit()
    conn.close()

def palyda(data):
    conn = sqlite3.connect('userdata.db')
    # conn.execute("insert or replace into playdata(cid, name, spc, sps, npc, nps, hpc, hps, epc, eps) select ?,?,?,?,?,?,?,?,?,? where not exists(select 1 from playdata where cid=? and name=?);",(data['cid'],data['name'],data['spc'],data['sps'],data['npc'],data['nps'],data['hpc'],data['hps'],data['epc'],data['eps'],data['cid'],data['name']))
    conn.execute("insert or replace into playdata(cid, name, spc, sps, npc, nps, hpc, hps, epc, eps) VALUES (?,?,?,?,?,?,?,?,?,? )",(data['cid'],data['name'],data['spc'],data['sps'],data['npc'],data['nps'],data['hpc'],data['hps'],data['epc'],data['eps']))
    conn.commit()
    conn.close()

def songdb():
    conn = sqlite3.connect('userdata.db')
    conn.execute('''
        create table if not exists songinfo
        (
                name         text     primary key not null,
                arts         text                 not null,
                bpm          text                 not null,
                gen          text                 not null,
                simple       INTEGER              not null,
                normal       INTEGER              not null,
                hard         INTEGER              not null,
                extra        INTEGER              not null,
                del          text              not null
        );
    ''')
    conn.commit()
    conn.close()

def gendb():
    conn = sqlite3.connect('userdata.db')
    conn.execute('''
        create table if not exists gen
        (
                gen          text     primary key not null,
                gentext      text                 not null
        );
    ''')
    conn.commit()
    conn.close()
    gendata()

def gendata():
    conn = sqlite3.connect('userdata.db')
    gentext={'animepops':'動漫/流行','vocaloid':'VOCALOID','touhou':'東方','otogame':'音樂遊戲','game':'遊戲','variety':'綜藝娛樂','original':'原創'}
    for key,value in gentext.items():
        conn.execute("insert or replace into gen(gen, gentext) VALUES (?,?)",(key,value))
        conn.commit()
    conn.close()

def selectmusic(musiccombo):
    conn = sqlite3.connect('userdata.db')
    conn = conn.cursor()
    conn.execute("select name, arts, bpm, gen, simple, normal, hard, extra, del from songinfo where name=?",(musiccombo,))
    data = conn.fetchone()
    print(data)
    return(data)
    conn.close

def upmusic(newdata):
    conn = sqlite3.connect('userdata.db')
    conn.execute("update songinfo set arts=?, bpm=?, gen=?, simple=?, normal=?, hard=?, extra=?, del=? where name=?",(newdata[1],newdata[2],newdata[3],newdata[4],newdata[5],newdata[6],newdata[7],newdata[8],newdata[0]))
    conn.commit()
    cn = conn.total_changes
    if cn == 0:
        return("error")
    else:
        return("OK")
    conn.close

def deletemusic(musiccombodata):
    conn = sqlite3.connect('userdata.db')
    conn.execute("delete from songinfo where name=?;",(musiccombodata,))
    conn.commit()
    connobj = conn.cursor()
    connobj.execute("select * from songinfo where name=?;",(musiccombodata, ))
    data = connobj.fetchone()
    if data is None:
        return('OK')
    elif data is not None:
        return('error')
    conn.close()

def selectmusic(musiccombodata):
    conn = sqlite3.connect('userdata.db')
    connobj = conn.cursor()
    connobj.execute("select * from songinfo where name=?;",(musiccombodata,))
    data = connobj.fetchone()
    if data is None:
        return('error')
    elif data is not None:
        connobj.execute("select * from songinfo where name=?;",(musiccombodata,))
        info = connobj.fetchone()
        return(info)
    else:
        print('db error')
        return('error')

def songdata(songinfo):
    conn = sqlite3.connect('userdata.db')
    # conn.execute("insert or replace into songinfo(name, arts, bpm, gen, simple, normal, hard, extra, del) select ?,?,?,?,?,?,?,?,? where not exists(select 1 from songinfo where name=?);",(songinfo['name'],songinfo['arts'],songinfo['bpm'],songinfo['gen'],songinfo['simple'],songinfo['normal'],songinfo['hard'],songinfo['extra'],songinfo['del'],songinfo['name']))
    conn.execute("insert or replace into songinfo(name, arts, bpm, gen, simple, normal, hard, extra, del) VALUES (?,?,?,?,?,?,?,?,?)",(songinfo['name'],songinfo['arts'],songinfo['bpm'],songinfo['gen'],songinfo['simple'],songinfo['normal'],songinfo['hard'],songinfo['extra'],songinfo['del']))
    conn.commit()
    conn.close()

def userinfodb():
    conn = sqlite3.connect('userdata.db')
    conn.execute('''
        create table if not exists info
        (
            cid         char(16) primary key not null,
            uid         text                 not null,
            tScore      text                 not null,
            aScore      text                 not null,
            pMusic      text                 not null,
            rank        text                 not null,
            avatar      text                 not null,
            title       text                 not null,
            clear       text                 not null,
            noMiss      text                 not null,
            fullChain   text                 not null,
            perfect     text                 not null,
            s           text                 not null,
            ss          text                 not null,
            sss         text                 not null,
            trophy      text                 not null,
            tRank       text                 not null
        );
    ''')
    conn.commit()
    conn.close()

def userinfo(userdata):
    conn = sqlite3.connect('userdata.db')
    userinfodb()
    # conn.execute("insert or replace into info(cid, uid, tScore, aScore, pMusic, rank, avatar, title, clear, noMiss, fullChain, perfect, s, ss, sss, trophy, tRank) select ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? where not exists(select 1 from info where cid=?);",(userdata["cid"],userdata["uid"],userdata["tScore"],userdata["aScore"],userdata["pMusic"],userdata["rank"],userdata["avatar"],userdata["title"],userdata["clear"],userdata["noMiss"],userdata["fullChain"],userdata["perfect"],userdata["s"],userdata["ss"],userdata["sss"],userdata["trophy"],userdata["tRank"],userdata["cid"]))
    conn.execute("insert or replace into info(cid, uid, tScore, aScore, pMusic, rank, avatar, title, clear, noMiss, fullChain, perfect, s, ss, sss, trophy, tRank) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(userdata["cid"],userdata["uid"],userdata["tScore"],userdata["aScore"],userdata["pMusic"],userdata["rank"],userdata["avatar"],userdata["title"],userdata["clear"],userdata["noMiss"],userdata["fullChain"],userdata["perfect"],userdata["s"],userdata["ss"],userdata["sss"],userdata["trophy"],userdata["tRank"]))
    conn.commit()
    conn.close()


def playdataget(CID,lv):
    conn = sqlite3.connect('userdata.db')
    connobj = conn.cursor()
    nameobj = conn.cursor()
    # connobj.execute("select name, spc, sps, npc, nps, hpc, hps, epc, eps from playdata where cid=?;",(CID,))
    nameobj.execute("select name from songinfo where (simple=? or normal=? or hard=? or extra=? and del='0');",(lv,lv,lv,lv))
    nrows = nameobj.fetchall()
    for row in nrows:
        name=str(row).replace("(","").replace(")","").replace("'","").replace(",","")
        # print(name)
        connobj.execute("select name, spc, sps, npc, nps, hpc, hps, epc, eps from playdata where (cid=? and name=?);",(CID,name))
        data = connobj.fetchone()
        if data is not None:
            print(data)
    # connobj.execute("select sps, nps, hps, eps, spc, npc, hpc, epc from playdata where cid=?;",(CID,))
    # rows = connobj.fetchall()
    # all=0
    # pl=0
    # for row in rows:
    #     if row[3]=="":
    #         allc=int(row[0])+int(row[1])+int(row[2])
    #     else:
    #         allc=int(row[0])+int(row[1])+int(row[2])+int(row[3])
    #     all=allc+all
    #     if row[7]=="":
    #         plc=int(row[4])+int(row[5])+int(row[6])
    #     else:
    #         plc=int(row[4])+int(row[5])+int(row[6])+int(row[7])
    #     pl=plc+pl
    # print(all)
    # print(pl)

def deleteinfo(cid):
    conn = sqlite3.connect('userdata.db')
    conn.execute("delete from info where cid=?;",(cid, ))
    conn.commit()
    connobj = conn.cursor()
    connobj.execute("select * from info where cid=?;",(cid, ))
    data = connobj.fetchone()
    if data is None:
        return('OK')
    elif data is not None:
        return('error')
    conn.close()

def deletepld(cid):
    conn = sqlite3.connect('userdata.db')
    conn.execute("delete from playdata where cid=?;",(cid,))
    conn.commit()
    connobj = conn.cursor()
    connobj.execute("select * from playdata where cid=?;",(cid, ))
    data = connobj.fetchone()
    if data is None:
        return('OK')
    elif data is not None:
        return('error')
    conn.close()

def showinfo(cid):
    conn = sqlite3.connect('userdata.db')
    connobj = conn.cursor()
    dataobj = conn.cursor()
    connobj.execute("select * from info where cid=?;",(cid, ))
    data = connobj.fetchone()
    if data is None:
        return('error')
    elif data is not None:
        connobj.execute("select * from info where cid=?;",(cid, ))
        info = connobj.fetchone()
        dataobj.execute("select spc,npc,hpc,epc from playdata where cid=?;",(cid, ))
        data = dataobj.fetchall()
        count=0
        for i in data:
            for u in i:
                count=count+u
        infodata=[]
        for i in info:
            infodata.append(i)
        infodata.append(count)
        return(infodata)
    else:
        print('db error')
        return('error')


def selectplayinfo(cid,gen,lv):
    lvint=int(lv)
    conn = sqlite3.connect('userdata.db')
    connobj = conn.cursor()
    dataobj = conn.cursor()
    connobj.execute("select * from songinfo where gen=?;",(gen, ))
    data = connobj.fetchone()
    infodata=[]
    if data is None:
        return('error')
    elif data is not None:
        connobj.execute("select * from songinfo where gen=?;",(gen, ))
        info = connobj.fetchall()
        for i in info:
            # if ((i[4]==lv or i[5]==lv or i[6]==lv or i[7]==lv) and i[8]=='0'):
            if ((i[4]==lvint or i[5]==lvint or i[6]==lvint or i[7]==lvint) and i[8]=='0'):
                dataobj.execute("select * from playdata where cid=? and name=?;",(cid,i[0]))
                playdata = dataobj.fetchone()
                if playdata is not None:
                    infodata.append(playdata[1])
        return(infodata)
    else:
        print('db error')
        return('error')

def selectplaydata(cid,name):
    conn = sqlite3.connect('userdata.db')
    connobj = conn.cursor()
    dataobj = conn.cursor()
    connobj.execute("select * from playdata where cid=? and name=?;",(cid,name))
    data = connobj.fetchone()
    if data is None:
        return('error')
    elif data is not None:
        dataobj.execute("select extra from songinfo where name=?;",(name, ))
        exin = dataobj.fetchone()
        connobj.execute("select * from playdata where cid=? and name=?;",(cid,name))
        exinfo=str(exin).replace("(","").replace(")","").replace("'","").replace(",","").replace("\n","").strip()
        info = connobj.fetchone()
        infodata=[]
        if exinfo=='0':
            for i in info:
                infodata.append(i)
            del infodata[-1]
            del infodata[-1]
            return(infodata)
        elif exinfo!='0':
            return(info)
    else:
        print('db error')
        return('error')
