from pymysql import *

hostname="localhost"
dbuser="root"
dbpass=""
dbname="webdevelopmentcourse"
conn=connect(hostname, dbuser, dbpass, dbname)
cursor=conn.cursor()

name='Mota Bhai'

str="update student set NAME='"+name+"' where ID=5"
res=cursor.execute(str)
conn.commit()
print(res)
conn.close()


