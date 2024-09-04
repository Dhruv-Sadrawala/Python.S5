def percentage(m,no_s):
	per=(m*100)/(no_s*100)
	print("Percentage are:",per)
	return (m*100)/(no_s*100)

def result(m,no_s):
	val=percentage(m,no_s)
	if val<33:
		print("Fail")
	else:
		print("Pass")

def display(enroll,name):
	print("Enrollment Number:",enroll)
	print("Name:",name)