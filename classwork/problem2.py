"""
	Student Attendance Problem
myfile.txt contents:

studentname: 0
studentname: 1
studentname: 0
studentname: 5
"""
f=open("myfile.txt")
while True:
	k=open("myfile.txt")
	studentdata=k.read()
	k.close()
	student=f.readline()
	if student=="\n":
		continue
	if not student:
		break
	s=student.split(": ")
	print(s[0])
	att=input("Attendance (p/a): ")
	if att=="p":
		temp=int(s[1])+1
		tempstr=s[0]+": "+str(temp)+"\n"
		tempstr=studentdata.replace(student, tempstr)
		g=open("myfile.txt", "w")
		g.write(tempstr)
		g.close()
f.close()
