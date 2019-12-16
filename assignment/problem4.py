class Student:
	def __init__(self, name, roll, presentdays):
		self.name =name 
		self.roll = roll
		self.presentdays = presentdays

studentlist=[
	Student("Yogassss", 69, 2),
	Student("R cheetah", 56, 16),
	Student("Root two za", 21, 5),
	Student("Pro 9", 9, 6),
	Student("She Vaani", 10, 16)
]

inproll=int(input("Chhatr ka anu kramank. Daalo: "))

s=""

for x in studentlist:
	if x.roll==inproll:
		s=x

nooftotaldays=16
attendeddays=s.presentdays

percent=float(attendeddays/nooftotaldays)*100

if percent<75:
	print("Defaulter madhe aali g bai / aala kartaa")
else:
	print("Vachlis tu / Vachlaas tu")









