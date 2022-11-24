'''
programe by MrUnKnown9871
python programe for school 

ALL PROGRAMES ARE COPYRIGHT FREE 

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


print('all oprations in lower case else stored in note')
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

# converting string from data
q1 = str(o1)
q2 = str(o2)
q3 = str(o3)

# merged string for time 
string1 = ""+q1+":"+q2+":"+q3+""

# main void loop

#  all exicute function for for loop
# extracting all sr no 



while(True):
    # collecting all databases
    mycur.execute('show databases')
    show_databases = mycur.fetchall()
    # stored result in show_databases
    
    # if database exists in the 
    if ('chat',) in show_databases:
        # added late if user may mess up with mysql command line 
        # using databse chat
        mycur.execute('use chat')
        mycur.execute('create table if not exists chat_base(sr_no int primary key auto_increment, time varchar(100),note varchar(8000),up_date_status varchar (10))')
        
        # delay is given for proframe loding time 
        time.sleep(0.25)

        # printing welcome fuction
        print("Welcome to KEEP NOTES")
        # notes quarry loop
        
        while(True):
            # taking note in input
            
            notes = input("Note : ")
            # stored datex (date function)
            
            

            if(notes == "delete" ):
                #conformation of deleteing function
                print('Entered in delete')
                # taking seriol number in input 
                delete_function = input("Enter the sr_no : ")
                # printing deleted seriol number
                print(delete_function)
                #delet function quarry
                quarry_dlete_function = 'delete from chat_base where sr_no = "'+delete_function+'"'
                # finally quarry deleted 
                mycur.execute(quarry_dlete_function)
                # deleting conformation statement
                print("Deleted the note if the given sr no is valid")
                mydb.commit()
            
            # not exit function    
            elif(notes != "exit"):
                # printing notes
                if(notes == "show"):
                    mycur.execute('select sr_no from chat_base')
                    sr_no_all = mycur.fetchall()
                                            # dtored sr no 
                                            #extracting all notes  
                    mycur.execute('select note from chat_base')
                    note_fetch_all = mycur.fetchall()
                                            # stored all notes 
                    mycur.execute('select time from chat_base')
                    TIME_INPUT = mycur.fetchall()

                    # extrexting recorded time of notes 
                    
                    # stored as time_input in lsit 
                    
                    length = len(TIME_INPUT)
                    # finding the length
                    # if length is zero nothing is printed 
                    
                    if length==0 :
                        print("No Notes found....")
                        continue
                    
                    # template of output formate 
                    print('sr no    Date time                 note    ')
                    # printing notes 
                    
                    for i in range(0,length):
                        

                        # variableise all using i from for loop
                        c = str(sr_no_all[i][0])
                        a = TIME_INPUT[i][0]
                        b = note_fetch_all[i][0]
                        # funis a variable displaying the records 
                        fun = ""+c+"        "+a+"  "+b+""
                        print(fun)

                # notes update function
                elif(notes == "update"):
                    # conformation msg for 
                    print('Welcome to update section')
                    
                    # taking user input (sr no)
                    user_inp = input("Enter the sr no : ")

                    # taking new note
                    new_note = input ("Enter the new note ")
                    
                    # updating function
                    mycur.execute('update chat_base set up_date_status="Edited",note ="'+new_note+'" where sr_no= "'+user_inp+'"')
                    mydb.commit()

                    # serious msg
                    print('Notes are updated if the given sr no is valid ')

                # note root function
                elif(notes == "history"):
                    
                    # selecting all data
                    mycur.execute('select * from chat_base')
                    
                    #storing all data
                    storage = mycur.fetchall()

                    # printing record 
                    for i in range(len(storage)):
                        
                        #printing record line by line  
                        print(storage[i])

                #inpput is given and stored in database
                elif(notes == "report"):
                    starting_date = input("Enter date : ")
                    for i in range(0,length):
                        mycur.execute('select sr_no from chat_base where time like "%'+starting_date+'%"')
                        abc  = mycur.fetchall()
                                                # dtored sr no 
                                                #extracting all notes  
                        mycur.execute('select note from chat_base where time like "%'+starting_date+'%"')
                        poi = mycur.fetchall()
                                                # stored all notes 
                        mycur.execute('select time from chat_base where time like "%'+starting_date+'%"')
                        sdf = mycur.fetchall()


                        # variableise all using i from for loop
                        c = str(abc [i][0])
                        a = sdf[i][0]
                        b = poi[i][0]
                        # funis a variable displaying the records 
                        qwert = ""+c+"        "+a+"  "+b+""
                        print(qwert)           
                else:
                    datex = str(string)
                    # stored timex (time function)
                    
                    timex = str(string1)
                    # storing string for giving input 
                    
                    time_date = ""+datex+"   "+timex+" > "
                    # delete function of note 
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

                    # converting string from data
                    q1 = str(o1)
                    q2 = str(o2)
                    q3 = str(o3)

                    # merged string for time 
                    string1 = ""+q1+":"+q2+":"+q3+""
                    # insert quarry
                    insert_into = 'insert into chat_base(time,note,up_date_status) value(%s,%s,"Orignal")'
                    val = [time_date,notes]
                    mycur.execute(insert_into,val)
                    mydb.commit()
            
            # not exit else function to exit 
            else:
                #exit
                exit()
    # else of not having database 
    else:
        #creating database
        mycur.execute("create database chat")
        #delay 
        time.sleep(0.25)
        
        #database create conformation statement
        print("Database Created")
        
        # using chat database to craete table 
        mycur.execute('use chat')
        
        # created table 
        mycur.execute('create table chat_base(sr_no int primary key auto_increment, time varchar(100),note varchar(8000),up_date_status varchar (10))')
        
        #delay
        time.sleep(0.25)
        #table craeted success mag
        print("Access Granted to store Notes ")
