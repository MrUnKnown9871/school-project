import mysql.connector
import time



# mydb = .connect(host="127.0.0.1",user=user1,passwd=passwd,database='chat')
    #  connecting to the server 


user_inp = input("Enter the USER NAME : ")
password_inp = input("Enter the PASSWORD : ")

mydb = mysql.connector.connect(host='localhost',user=user_inp,passwd=password_inp)
mycur = mydb.cursor()
# # creating cursor 
# mycur.execute('create database if not exists chat')

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



while(True):
    # cheaing for database existence 
    mycur.execute('show databases')
    show_databases = mycur.fetchall()
    if ('chat',) in show_databases:
        mycur.execute('use chat')
        time.sleep(0.25)
        print("Welcome to KEEP NOTES")

        
        while(True):
            # function string for cheaking for delete code 
            notes = input("Note : ")
            
            
            # function for temp time and date 
            datex = str(string)
            timex = str(string1)
            time_date = ""+datex+"   "+timex+" > "
            
           

            if(notes == "delete" ):
                print('Entered in delete')
                tim_input = input("Enter the time (hour:minute:second): ")
                date_input = input("Enter the date (dd/mm/yyyy): ")
                time_date_delete_function = ""+date_input+"   "+tim_input+" > "
                print(time_date_delete_function)
                quarry_dlete_function = 'delete from chat_base where time = "'+ time_date_delete_function+'"'
                mycur.execute(quarry_dlete_function)
                print("Deleted sucessfully")
                mydb.commit()
                
            elif(notes != "exit"):
                if(notes == "show"):
                    
                    mycur.execute('select time from chat_base')

                    TIME_INPUT = mycur.fetchall()

                    length = len(TIME_INPUT)

                    mycur.execute('use chat')


                    mycur.execute('select time from chat_base')

                    TIME_INPUT = mycur.fetchall()

                    length = len(TIME_INPUT)

                    if length==0 :
                        print("No Notes found....")
                        continue

                    print(' sr no     Date time         note    ')
                    list_of_msg = []
                    list_of_time  = []

                    for i in range(0,length):
                        
                        # mydb = mysql.connector.connect(host='localhost',user=user_inp,passwd=password_inp ,database='chat')
                        # mycur = mydb.cursor()
                        mycur.execute('select time from chat_base')

                        TIME_INPUT = mycur.fetchall()
                        # print(TIME_INPUT)
                        mycur.execute('select note from chat_base')
                        note_fetch_all = mycur.fetchall()
                        # print(note_fetch_all)
                        a = TIME_INPUT[i][0]
                        # print(a)

                        b = note_fetch_all[i][0]
                        # print(b)    
                        fun = ""+a+"    "+b+""
                        print(fun)
                
                else:
                    insert_into = 'insert into chat_base(time,note) value(%s,%s)'
                    val = [time_date,notes]
                    mycur.execute(insert_into,val)
                    mydb.commit()
                    
                    

            else:
                exit()

    else:

        # createing databases
        mycur.execute("create database chat")
        time.sleep(0.25)
        print("Database Created")
        # using databases
        mycur.execute('use chat')
        # created table 
        mycur.execute('create table chat_base(sr_no int primary key auto_increment, time varchar(100),note varchar(8000))')
        time.sleep(0.25)
        print("Chat created successfully")
        # exit()
