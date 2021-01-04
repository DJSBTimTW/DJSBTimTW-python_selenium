import sqlite3

def playdb():
    conn = sqlite3.connect('userdata.db')
    conn.execute('''
        create table if not exists playdata
        (
                cid          char(16)  not null,
                name         text      not null,
                spc          text                 not null,
                sps          text                 not null,
                npc          text                 not null,
                nps          text                 not null,
                hpc          text                 not null,
                hps          text                 not null,
                epc          text                 not null,
                eps          text                 not null,
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
                simple       text                 not null,
                normal       text                 not null,
                hard         text                 not null,
                extra        text                 not null,
                del          text                 not null
        );
    ''')
    conn.commit()
    conn.close()

def songdata(songinfo):
    conn = sqlite3.connect('userdata.db')
    # conn.execute("insert or replace into songinfo(name, arts, bpm, gen, simple, normal, hard, extra, del) select ?,?,?,?,?,?,?,?,? where not exists(select 1 from songinfo where name=?);",(songinfo['name'],songinfo['arts'],songinfo['bpm'],songinfo['gen'],songinfo['simple'],songinfo['normal'],songinfo['hard'],songinfo['extra'],songinfo['del'],songinfo['name']))
    conn.execute("insert or replace into songinfo(name, arts, bpm, gen, simple, normal, hard, extra, del) VALUES (?,?,?,?,?,?,?,?,?)",(songinfo['name'],songinfo['arts'],songinfo['bpm'],songinfo['gen'],songinfo['simple'],songinfo['normal'],songinfo['hard'],songinfo['extra'],songinfo['del']))
    conn.commit()
    conn.close()

def userinfo(userdata):
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


