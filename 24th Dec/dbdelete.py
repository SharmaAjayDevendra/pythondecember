from pymysql import *

hostname="localhost"
dbuser="root"
dbpass=""
dbname="webdevelopmentcourse"
conn=connect(hostname, dbuser, dbpass, dbname)
cursor=conn.cursor()

str="delete from student where ID=5"
res=cursor.execute(str)
conn.commit()
print(res)
conn.close()


