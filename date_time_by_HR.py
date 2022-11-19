import mysql.connector
myd = mysql.connector.connect(host='localhost',user='root',passwd='root')
mycur = myd.cursor()
def date1():
    mycur.execute('select  day(now()),month(now()),year(now())')
    q = mycur.fetchall()
    i1 = q[0][0]
    i2 = q[0][1]
    i3 = q[0][2]
    a = str(i1)
    b = str(i2)
    c = str(i3)
    string = ""+a+"/"+b+"/"+c+""
    return string
# test comment
def time1():
    mycur.execute('select hour(now()),minute(now()),second(now())')
    x = mycur.fetchall()
    o1 = x[0][0]
    o2 = x[0][1]
    o3 = x[0][2]
    q1 = str(o1)
    q2 = str(o2)
    q3 = str(o3)
    string1 = ""+q1+":"+q2+":"+q3+""
    return string1