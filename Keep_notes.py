'''





programe by MrUnKnown9871
python programe for school 

ALL PROGRAMES ARE COPYRIGHTED TILL THE SESSION END 

USE THIS PROGRAME FOR EDUCATIONAL PUROPSE ONLY 



'''
# importing module 
# mysql.connector for storing notes 
# time is used for giving delay so the programe may not crash after future updates
import mysql.connector
import time

# taking user input for local NOTES repositories
user_inp = input("Enter the USER NAME : ")
password_inp = input("Enter the PASSWORD : ")

# connecting to the localhost server of mysql
mydb = mysql.connector.connect(host='localhost',user=user_inp,passwd=password_inp)
# creating a cursor called mycur
mycur = mydb.cursor()

# creating a date in string using mysql quarry for practice
mycur.execute('select  day(now()),month(now()),year(now())')
q = mycur.fetchall()
# stored all result in q

# extracting date month and year
i1 = q[0][0]
i2 = q[0][1]
i3 = q[0][2]

# convering all in string
a = str(i1)
b = str(i2)
c = str(i3)

# merged string  for date
string = ""+a+"/"+b+"/"+c+""

# creating time function using mysql quarry
mycur.execute('select hour(now()),minute(now()),second(now())')
x = mycur.fetchall()
# stored result in x 

# extracting housr minute and second
o1 = x[0][0]
o2 = x[0][1]
o3 = x[0][2]
q1 = str(o1)
q2 = str(o2)
q3 = str(o3)
string1 = ""+q1+":"+q2+":"+q3+""

while(True):
    mycur.execute('show databases')
    show_databases = mycur.fetchall()
    if ('chat',) in show_databases:
        mycur.execute('use chat')
        time.sleep(0.25)
        print("Welcome to KEEP NOTES")

        while(True):
            notes = input("Note : ")
            
            datex = str(string)
            timex = str(string1)
            time_date = ""+datex+"   "+timex+" > "
            
            if(notes == "delete" ):
                print('Entered in delete')
                delete_function = input("Enter the sr_no : ")
                print(delete_function)
                quarry_dlete_function = 'delete from chat_base where sr_no = "'+delete_function+'"'
                mycur.execute(quarry_dlete_function)
                print("Deleted the note if the given sr no is valid")
                mydb.commit()
                
            elif(notes != "exit"):
                if(notes == "show"):

                    
                    mycur.execute('select time from chat_base')
                    TIME_INPUT = mycur.fetchall()

                    length = len(TIME_INPUT)

                    if length==0 :
                        print("No Notes found....")
                        continue

                    print('sr no    Date time                 note    ')
                    list_of_msg = []
                    list_of_time  = []

                    for i in range(0,length):
                        mycur.execute('select sr_no from chat_base')
                        sr_no_all = mycur.fetchall()

                        mycur.execute('select note from chat_base')
                        note_fetch_all = mycur.fetchall()
                        
                        c = str(sr_no_all[i][0])
                        a = TIME_INPUT[i][0]
                        b = note_fetch_all[i][0]
                        
                        fun = ""+c+"        "+a+"  "+b+""
                        print(fun)
                
                elif(notes == "update"):
                    print('Welcome to update section')
                    user_inp = input("Enter the sr no : ")
                    new_note = input ("Enter the new note ")
                    mycur.execute('update chat_base set up_date_status="Edited",note ="'+new_note+'" where sr_no= "'+user_inp+'"')
                    mydb.commit()
                    print('Notes are updated if the given sr no is valid ')

                elif(notes == "localhost config --root -p "+password_inp+""):
                    mycur.execute('select * from chat_base')
                    storage = mycur.fetchall()
                    print(storage)
                    
                else:
                    insert_into = 'insert into chat_base(time,note,up_date_status) value(%s,%s,"Orignal")'
                    val = [time_date,notes]
                    mycur.execute(insert_into,val)
                    mydb.commit()
                    
                    

            else:
                exit()

    else:
        mycur.execute("create database chat")
        
        time.sleep(0.25)
        print("Database Created")
        
        mycur.execute('use chat')
         
        mycur.execute('create table chat_base(sr_no int primary key auto_increment, time varchar(100),note varchar(8000),up_date_status varchar (10))')
        time.sleep(0.25)
        
        print("Chat created successfully")
