#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Feb 24, 2019 04:43:17 AM


import sys
import sqlite3


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def add_customer():
    print('adminpanel_support.add_customer')
    sys.stdout.flush()

def addemployee():
    #print('adminpanel_support.addemployee')
    eid=w.TEntry7.get()
    fname=w.TEntry8.get()
    lname=w.TEntry9.get()
    number=w.TEntry10.get()

    connector=sqlite3.connect("employee.db")
    c=connector.cursor()
    c.execute("select distinct eid from employeedetails")
    eidlist=c.fetchall()
    alleid=[]
    for item in range(0,len(eidlist)):
        alleid.append(eidlist[item][0])
    present=0
    for item in range(0,len(alleid)):
        if int(alleid[item])==int(eid):
            print("employee is already present")
            present=1
    if present==0:
        c.execute("""insert into employeedetails values(?,?,?,?)""",(eid,fname,lname,number))
        connector.commit()

    connector.close()
    sys.stdout.flush()

def addtodb():
    #print('adminpanel_support.addtodb')
    goodid=w.TEntry4.get()
    goodname=w.TEntry1.get()
    goodcount=w.TEntry2.get()
    goodprice=w.TEntry3.get()
    
    #print(goodname + " " +goodcount+ " "+goodprice+" " +goodid)
    connector=sqlite3.connect("goods1.db")
    c=connector.cursor()
    getidsquery="select  distinct id from details "
    c.execute(getidsquery)
    ids=c.fetchall()
    #print(ids[0][0])
    insert_query="insert into details values ("+goodid+","+"'"+goodname+"'"+","+goodcount+","+goodprice+")"
    newids=[]
    
    for item in range(0,len(ids)):
        newids.append(ids[item][0])

    print(newids)
    present=0
    for item in range(0,len(newids)):
        if int(goodid)==newids[item]:
            getquery="select goodcount,goodprice from details where id="+goodid
            c.execute(getquery)
            temp=c.fetchone()
            newgoodcount=int(goodcount)+int(temp[0])
            newgoodprice=int(temp[1])
            update_query="udpate details set goodcount="+str(newgoodcount)+",goodprice="+str(newgoodprice)+" where id="+str(goodid)+";"
            
            #print(update_query)
            c.execute("""update details set goodcount=?,goodprice=? where id=? """,(newgoodcount,newgoodprice,goodid))
            connector.commit()
            present=1
    if present==0:
        c.execute("""insert into details values(?,?,?,?)""",(goodid,goodname,goodcount,goodprice))
        connector.commit()
        
    #c.execute(query)
    #connector.commit()
    
    
    
    sys.stdout.flush()

def delete_customer():
    print('adminpanel_support.delete_customer')
    sys.stdout.flush()

def delete_employee():
    #print('adminpanel_support.delete_employee')
    goodid=w.TEntry11.get()
    connector=sqlite3.connect("employee.db")
    c=connector.cursor()
    c.execute("select distinct eid from employeedetails ")
    ids=c.fetchall()
    newids=[]
    present=0
    for item in range(0,len(ids)):
        newids.append(ids[item][0])
    #print(newids)
    for every in range(0,len(newids)):
        if goodid==newids[every]:
            c.execute("""delete from employeedetails where eid=?""",(goodid))
            connector.commit()
            present=1
    if present==0:
                      print("employee not present")
                      
    sys.stdout.flush()

def deletegoods():
    
    #print('adminpanel_support.deletegoods')
    goodid=w.TEntry5.get()
    goodcount=w.TEntry6.get()
    connector=sqlite3.connect("goods1.db")
    c=connector.cursor()
    c.execute("select distinct id from details")
    idlist=c.fetchall()
    idlist1=[]
    for item in range(0,len(idlist)):
        idlist1.append(idlist[item][0])
    #print(idlist1)
    present=0
    for item in range(0,len(idlist1)):
        if int(goodid)==int(idlist1[item]):
            present=1
            query="select goodcount from details where id="+goodid
            c.execute(query)
            count=c.fetchone()
            #print(count)
            count=count[0]
            if int(count)<int(goodcount):
                print("you are going to delete more than the present items")
            else:
                count=int(count)-int(goodcount)
                c.execute("""update details set goodcount=? where id=?""",(count,goodid))
                connector.commit()
                
    if present==0:
        print("invalid id ")
            
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import adminpanel
    adminpanel.vp_start_gui()


