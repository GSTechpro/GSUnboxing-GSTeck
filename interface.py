import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost',
                      user='root',
                      passwd='gowrishankar@123',
                      database='collegemanagement')
if mycon.is_connected()== False:
    print('Error connecting to Mysql database')

Mycursor=mycon.cursor()

Mycursor.execute("select * from students",
                 "select * from professors")

queries=Mycursor.fetchall()
nrec=Mycursor.rowcount
print("Total number of rows retrieved so far from resultset :", nrec )
for m,o,t,h,e,r in queries:
    print(m,o,t,h,e,r)
#queries=Mycursor.fetchone()
#count=Mycursor.rowcount
#print("Total number of rows retrieved so far from resultset :", count )

#queries=Mycursor.fetchall()
#count=Mycursor.rowcount
#print("Total number of rows retrieved so far from resultset :", count )
