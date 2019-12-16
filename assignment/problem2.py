class Product:
	def __init__(self, title, price, weight):
		self.title=title
		self.price=price
		self.weight=weight

productlist=[Product("Burger", "60", "1"), Product("Pizza", "260", "1.5"), Product("Fair and Lovely", "50", "5")]
total=0
totalweight=0
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
	totalweight=totalweight+float(productlist[pinp-1].weight)



state=input("Enter State: \n1. Maharashtra\n2. Other\n")
shippingcharges=0
if state=="1":
	if totalweight>=5:
		shippingcharges=60
	elif totalweight>=2:
		shippingcharges=80
	elif totalweight>=1:
		shippingcharges=100
	else:
		shippingcharges=0
elif state=="2":
	if totalweight>=5:
		shippingcharges=200
	elif totalweight>=2:
		shippingcharges=270
	elif totalweight>=1:
		shippingcharges=300
	else:
		shippingcharges=0



print("Total: Rs. "+str(total+shippingcharges)+"/-")







