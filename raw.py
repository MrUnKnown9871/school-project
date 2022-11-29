import mysql.connector
import time 


mydb = mysql.connector.connect(host='localhost',user='root',passwd="Root")
mycur = mydb.cursor()


mycur.execute('create database if not exists note')
mycur.execute('use note')
mycur.execute('create table if not exists userMaster(uid varchar(10),password varchar(50))')

mycur.execute("Select * from userMaster")
if(len(mycur.fetchall())==0):
    mycur.execute("insert into userMaster value('Harsh','123456')")
    mycur.execute("insert into userMaster value('Master','111111')")
    mycur.execute("insert into userMaster value('Mohit','654321')")
    mycur.execute("insert into userMaster value('Mishra','123456')")

mycur.execute('create table if not exists chat_base(sr_no int primary key auto_increment, time varchar(100),note varchar(8000),up_date_status varchar (10), user varchar(50))')

user_id = input('Enter the User Id : ')
passwd = input('Enter the Password : ')
mycur.execute("Select * from userMaster where uid='"+user_id+"' and password='"+passwd+"'")
if(len(mycur.fetchall())>0):
    while True:
        print('Welcome To Keep Notes ...')
        print('type "/help" to get help')

        while True:
            notes = input('Enter The Note : ')

            if (notes == "delete"):
                print('Entered in delete')

                delete_function = input("Enter the sr_no : ")
                print(delete_function)

                quarry_dlete_function = 'delete from chat_base where sr_no = "'+delete_function+'"'
                mycur.execute(quarry_dlete_function)

                print("Deleted the note if the given sr no is valid")
                mydb.commit()

            elif(notes == "/help"):
                print('Enter any note and press ENTER to store ')
                print('write the notes in any character ')
                print('All Commands are in lower case be careful while using ..')
                print('Eg. Store "update" as "Update"')
                print('Type exit to exit in notes "DO NOT USE INSIDE ANY FUNCTION ONLY USED FROM NOTES INPUT PLACE "')
                print("ALL COMMANDS ARE AS FOLLOW \n1 'show' to show all notes \n2 'update' to update \n3 'delete' to delete note \n4 'report' to display  report \n5 'history' to show history \n6 'logout' to logout")
            
            elif(notes == "show"):
                mycur.execute('select sr_no from chat_base')
                sr_no_all = mycur.fetchall() 

                mycur.execute('select note from chat_base')
                note_fetch_all = mycur.fetchall()

                mycur.execute('select time from chat_base')
                TIME_INPUT = mycur.fetchall()

                length = len(TIME_INPUT)    

                if length==0 :
                    print("No Notes found....")
                    continue

                print('sr no    Date time                 note    ')

                for i in range(0,length):
                    c = str(sr_no_all[i][0])
                    a = TIME_INPUT[i][0]
                    b = note_fetch_all[i][0]

                    fun = ""+c+"        "+a+"  "+b+""
                    print(fun)

            elif(notes == "history"):
                mycur.execute('select * from chat_base')
                storage = mycur.fetchall()
                length1 = len(storage)    

                if length1==0 :
                    print("No Notes found....")
                    continue

                for i in range(len(storage)):  
                            print(storage[i])

            elif(notes == "update"):
                mycur.execute('select * from chat_base')
                temp = mycur.fetchall()
                if len(temp)==0:
                    print("No Notes found....")
                    
                else:
                    print('Welcome to update section')

                    user_inp = input("Enter the sr no : ")
                    new_note = input ("Enter the new note ")

                    mycur.execute('update chat_base set up_date_status="Edited",note ="'+new_note+'" where sr_no= "'+user_inp+'"')
                    mydb.commit()

                    print('Notes are updated if the given sr no is valid ')

            elif(notes == "report"):
                d_t = input('Enter the Time or Date : ')

                mycur.execute('select sr_no from chat_base where time like "%'+d_t+'%" and user="'+user_id+'"')
                sr_no_all = mycur.fetchall()

                mycur.execute('select note from chat_base where time like "%'+d_t+'%"')
                note_fetch_all = mycur.fetchall()

                mycur.execute('select time from chat_base where time like "%'+d_t+'%"')
                TIME_INPUT = mycur.fetchall()

                length = len(TIME_INPUT)

                if length==0 :
                    print("No Notes found....")
                    continue

                print('sr no    Date time                 note    ')

                for i in range(0,length):
                    c = str(sr_no_all[i][0])
                    a = TIME_INPUT[i][0]
                    b = note_fetch_all[i][0]

                    fun = ""+c+"        "+a+"  "+b+""
                    print(fun)

            elif(notes == "logout"):
                exit()

            else:
                mycur.execute('select  day(now()),month(now()),year(now())')
                q = mycur.fetchall()
                
                i1 = q[0][0]
                i2 = q[0][1]
                i3 = q[0][2]
                
                a = str(i1)
                b = str(i2)
                c = str(i3)
                
                string = ""+a+"/"+b+"/"+c+""
                
                mycur.execute('select hour(now()),minute(now()),second(now())')
                x = mycur.fetchall()
                
                o1 = x[0][0]
                o2 = x[0][1]
                o3 = x[0][2]
                
                q1 = str(o1)
                q2 = str(o2)
                q3 = str(o3)
                
                string1 = ""+q1+":"+q2+":"+q3+""
                
                datex = str(string)
                timex = str(string1)
                
                time_date = ""+datex+"   "+timex+" > "
                
                insert_into = 'insert into chat_base(time,note,up_date_status,user) value(%s,%s,"Orignal",%s)'
                
                val = [time_date,notes,user_id]
                
                mycur.execute(insert_into,val)
                mydb.commit()
else:
    print("Invalid User Id or Password")