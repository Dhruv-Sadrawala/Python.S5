n1=int(input("Enter a number other than 3: "))
try:
	if n1==3:
		raise Exception
except Exception:
	print("You choosed in exception ",n1)
else:
	print("You choosed ",n1)
finally:
	print("Thankyou for entering number.")