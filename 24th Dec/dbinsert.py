from pymysql import *

hostname="localhost"
dbuser="root"
dbpass=""
dbname="webdevelopmentcourse"
conn=connect(hostname, dbuser, dbpass, dbname)
cursor=conn.cursor()

name='Pratik'
email='pratik@gmail.com'
address='Thane'
password='password123'

str="insert into student(NAME, EMAIL, ADDRESS, PASSWORD) values('"+name+"', '"+email+"', '"+address+"', '"+password+"')"
res=cursor.execute(str)
conn.commit()
print(res)
conn.close()


