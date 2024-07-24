print("Enter 1 for Employee")
print("Enter 2 for Star")
print("Enter 3 for Student Dictionary")

ch=int(input("Enter Choice:"))


if ch==1:


	employee_details=[]
	employee_id=int(input('Enter a ID:'))
	employee_name=(input('Enter Name:'))
	employee_sal=int(input('Enter Salary:'))
	employee_dept=(input('Enter Department:'))
	hra=0
	med=0

	if employee_sal > 80000:
		hra=employee_sal*1.1;
		med=employee_sal*1.15;
		print("HRA is:",hra);
		print("Mediclaim",med);

	elif employee_sal > 50000:
		hra=employee_sal*0.7;
		med=employee_sal*1.2;
		print("HRA is:",hra);
		print("Mediclaim",med);

	elif employee_sal > 30000:
		hra=employee_sal*0.5;
		med=employee_sal*1.0;
		print("HRA is:",hra);
		print("Mediclaim",med);

		employee_details=[employee_id,employee_name,employee_sal,employee_dept]
		print("Employee Name:",{employee_details[1]})
		print("Employee Department:",{employee_details[3]})


elif ch == 2:

	i=int(input('Enter Starting '))
	j=int(input("Enter Ending "))


	for i in range(i,j+1):
		for j in range(j+1):
			if j < i:
				print("*",end=" ")
		print(" ")


elif  ch==3:

	student_dictionary={"Name":"ABC","Roll_No":12,"Contact":45522154,"Email":"vhdvw@gmail.com"}
	print('Roll_No' in student_dictionary)
	print(student_dictionary)