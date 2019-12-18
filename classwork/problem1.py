totalprice=0
while True:
	inp=input("MENU:\n1. Purchase Product\n2. Checkout\n")
	if inp=="2":
		break
	f=open("myfile.txt")

	counter=0
	while True:
		counter+=1
		s=f.readline()
		if not s:
			break
		print(s.replace("Name:", str(counter)+"."), end="")
	print()
	f.close()

	p=int(input("Select a product: "))

	f=open("myfile.txt")
	counter=0
	while True:
		counter+=1
		s=f.readline()
		if not s:
			break
		if counter==p:
			temp=s.replace("Name: ", "").replace("Price: ", "").split(", ")
			totalprice+=int(temp[1])
	f.close()

print("Total Pricing: Rs. "+ str(totalprice)+"/-")





