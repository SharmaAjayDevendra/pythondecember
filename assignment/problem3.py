class User:
	def __init__(self, name, email, contact, dob, password):
		self.name=name
		self.email=email
		self.contact=contact
		self.dob=dob
		self.password=password

userlist=[]
while True:
	inp=input("1. Sign Up\n2. Log In\n3.Exit\n")

	if inp=="1":
		name=input("Enter Name: ")
		email=input("Enter Email: ")
		contact=input("Enter Contact: ")
		dob=input("Enter Birth Date: ")
		password=input("Enter Password: ")
		u=User(name, email, contact, dob, password)
		userlist.append(u)
	elif inp=="2":
		email=input("Enter Email: ")
		password=input("Enter Password: ")
		isError=True
		for x in userlist:
			if x.email==email and x.password==password:
				isError=False

		if not isError:
			print("Logged in successfully")
		else:
			print("Invalid Log In")
	else:
		break





