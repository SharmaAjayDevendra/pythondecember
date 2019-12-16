class Product:
	def __init__(self, title, price):
		self.title=title
		self.price=price

productlist=[Product("Burger", "60"), Product("Pizza", "260"), Product("Fair and Lovely", "50")]
total=0

while True:

	inp=input("1. Purchase Product\n2. Checkout\n")

	if inp=="2":
		break
	print()

	counter=0

	for x in productlist:
		counter = counter+1
		temp=str(counter)+". "+x.title+" - Rs. "+x.price+"/-"
		print(temp)

	print()

	pinp=int(input("Enter Product ID: "))
	total=total+int(productlist[pinp-1].price)


print("Total: Rs. "+str(total)+"/-")







