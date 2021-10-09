import MySQLdb as db #importing MySQLdb
#establishing connection to local host 
con=db.connect(host="localhost",user="root",password="")
cur=con.cursor()
#creating database
def createdb():
    s="create database event_management_db"
    cur.execute(s)
    cur.close()
    con.close()
    print("Database is created successfully")
 #creating table in database
def create_table():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="CREATE TABLE events(name varchar(30),event_id int,event_name varchar(30) not null,event_place varchar(30) not null,event_time timestamp not null,PRIMARY KEY(event_id ))"
    cur.execute(query)
    cur.close()
    con.close()
    print("table created successfully")
 #adding events to created table
def add_event():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="insert into events values('Sonu',1,'birthday_event','Rk-beach','2021-12-26 03:00:00')"
    cur.execute(query)
    query="insert into events values('sravani',2,'marriage_event','Gadiraju_Palace','2025-2-12 2:00:00')"
    cur.execute(query)
    query="insert into events values('Siri',3,'sungeeth_event','Rushi_konda','2027-11-12 11:30:00')"
    cur.execute(query)
    query="insert into events values('sameera',4,'fest_event','vijayawada','2021-10-15 2:30:00')"
    cur.execute(query)
    query="insert into events values('Gayathri',5,'diwali_event','nuzvid','2021-11-05 10:20:00')"
    cur.execute(query)
    query="insert into events values('Teju',6,'engagement','East-godavari','2021-3-15 12:30:00')"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    print("rows are inserted")
 #updating events in a table
def update_event():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="update events set name='Tejasri' where event_id=6"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()
    print("updated")
 #deleting an events in a table
def delete_event():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="delete from events where event_id=5"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()
    print("deleted")
 #dispalying all events
def display_event():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="select * from events"
    cur.execute(query)
    data=cur.fetchall()
    #print(data)
    print(cur.rowcount)
    col=[i[0] for i in cur.description]
    for i in col:
        print(i,end=" ")
    print("-----------") 
    for i in data:
        for j in i:
            print(j,end=",")
        print()
 #searching an event_type by name
def search_by_event_type_and_name(name,event_type):
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="select * from events where name='"+name+"' and event_name='"+event_type+"'"
    cur.execute(query)
    data=cur.fetchall()
    if data:
        print(data)
    else:
        print("search name and event not here")
    cur.close()
    con.close()
#upcoming events in next 7 days
def next_7_days_upcoming():
    con=db.connect(host="localhost",user="root",password="",database="event_management_db")
    cur=con.cursor()
    query="select * from events WHERE DATE(event_time) > CURDATE() + INTERVAL 7 DAY"
    data=cur.execute(query)

    if data:
     print(data)
    else:
        print("there are no events")
    cur.close()
    con.close()

#user interaction  by selecting an option in command prompt
while True:
    print("1.create Database")
    print("2.create table")
    print("3.adding_event")
    print("4.update_event")
    print("5.delete_event")
    print("6.display_events")
    print("7.search_by_event_type")
    print("8.upcoming_events")
    print("9.Exit")
    ch=int(input("enter ur choice:"))
    if(ch==1):
        createdb()
    elif(ch==2):
        create_table()

    elif(ch==3):
        add_event()
    elif(ch==4):
        update_event()
    elif(ch==5):
        delete_event()
    elif(ch==6):
        display_event()
    elif(ch==7):
        name=input("enter the name")
        event_type=input("enter event_type")
        search_by_event_type_and_name(name,event_type)
    elif(ch==8):
        next_7_days_upcoming()
    else:
        break
    
    
