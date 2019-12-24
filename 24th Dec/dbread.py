from pymysql import *

hostname="localhost"
dbuser="root"
dbpass=""
dbname="webdevelopmentcourse"
conn=connect(hostname, dbuser, dbpass, dbname)
cursor=conn.cursor()

cursor.execute("select *from student")
row=cursor.fetchall()

for x in row:
	print(x)

conn.close()
