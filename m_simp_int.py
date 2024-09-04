def simple_intrest(p,r,n):
	interest = (p*r*i)/100
	print("Interest is :",interest)

def deposit(bal,amount):
	curr_amt=bal+amount
	print("Amount after deposit:",curr_amt)
	if curr_amt>50000:
		interest_onac=(amount*5)/100
		print("Balance is greater than 50000:",interest_onac+amount)

def withdrawl(bal,amount):
	print("Amount after withdrawl:",bal-amount)