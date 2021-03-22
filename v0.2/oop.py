class Student:
	def __init__ (self, name, surname, age, course):
		self.name = name
		self.surname = surname
		self.age = age
		self.course = course
		self.salary = 1000

	def get_older(self, years = 1):
		self.age += years
		self.course += years

	def add_salary(self, price):
		self.salary += price
	
	def check_age(self, other_obj):
		if (self.age > other_obj.age):
			print(f"{self.name} is Older than {other_obj.name}")
		if (self.age < other_obj.age):
			print(f"{other_obj.name} is Older than {self.name}")


mike = Student(
	name = "Muhammed",
	surname = "Jepbarov",
	age = 22,
	course = 3
)

mekan = Student(
	name = "Mekan",
	surname = "Hojaberiev",
	age = 20,
	course = 2
)

mekan.age = 33
mike.check_age(mekan)


print(f"AGE: {mike.age} | COURSE: {mike.course}")
mike.get_older(years = 8)
print(f"AGE: {mike.age} | COURSE: {mike.course}")

print(f"salary: {mike.salary}")
mike.add_salary(price = 10)
print(f"salary: {mike.salary}")