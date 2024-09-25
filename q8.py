class student:
	def __init__(self,name,age,degree):
		self.name=name
		self.age=age
		self.degree=degree

		print("Name:",name)
		print("Age:",age)
		print("Degree:",degree)





name1=input("Enter name of student 1:")
age1=int(input("Enter age of student 1:"))
degree1=input("Enter degree of student 1:")

student1=student(name1,age1,degree1)

name2=input("Enter name of student 2:")
age2=int(input("Enter age of student 2:"))
degree2=input("Enter degree of student 2:")

student2=student(name2,age2,degree2)