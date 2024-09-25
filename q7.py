n1=int(input("Enter a non-negative number: "))
try:
	if n1<0:
		raise ValueError
except ValueError:
	print("You choosed {0} which is a negative number.".format(n1))
else:
	print("You choosed {0} which is a positve number.".format(n1))