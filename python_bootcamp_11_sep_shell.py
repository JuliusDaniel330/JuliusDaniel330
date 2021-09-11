Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,4,5]
[1, 2, 4, 5]
>>> [1, 2, 4, 5].index(4)
2
>>> [1, 2, 4, 5].remove(4)
>>> type(list)
<class 'type'>
>>> 
>>> 
>>> type(['ajdk'])
<class 'list'>
>>> type(2)
<class 'int'>
>>> 2
2
>>> class Dog:
	pass

>>> bingo = Dog()
>>> bing0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    bing0
NameError: name 'bing0' is not defined
>>> bingo
<__main__.Dog object at 0x7f9cf834ebe0>
>>> type(bingo)
<class '__main__.Dog'>
>>> bingo.name = 'bingo'
>>> bingo.age = 6
>>> bingo.name
'bingo'
>>> bingo.age
6
>>> 
>>> bingo.height
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    bingo.height
AttributeError: 'Dog' object has no attribute 'height'
>>> bingo.height = 22
>>> bingo.height
22
>>> class Dog:
	name = ""
	age = 0

	
>>> bingo = Dog()
>>> bingo.name
''
>>> bingo.age
0
>>> ken = Dog()
>>> ken.age
0
>>> ken.name
''
>>> ken.name = 'ken'
>>> ken.name
'ken'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class Dog:
	name = 'kenny'
	color = 'black'
	age = 6

	
>>> class Dog:
	name = 'kenny'
	color = 'black'
	age = 6
	def bark():
		print("woof woof")

		
>>> kenny = Dog()
>>> kenny
<__main__.Dog object at 0x7f9cf834ebe0>
>>> kenny.name
'kenny'
>>> kenny.color
'black'
>>> kenny.age
6
>>> kenny.bark()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    kenny.bark()
TypeError: bark() takes 0 positional arguments but 1 was given
>>> class Dog:
	name = 'kenny'
	color = 'black'
	age = 6
	def bark(self):
		print("woof woof")

		
>>> kenny = Dog()
>>> kenny.name
'kenny'
>>> kenny.color
'black'
>>> kenny.age
6
>>> kenny.bark()
woof woof
>>> age = []
>>> age
[]
>>> age.append(60)
>>> age
[60]
>>> ages = list()
>>> ages
[]
>>> bingo = Dog()
>>> bingo.name
'kenny'
>>> bingo.color
'black'
>>> bingo.name = 'bingo'
>>> bingo.name
'bingo'
>>> age = [89]
>>> back = list()
>>> class Dog:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
	def bark(self):
		print("woof woof")

		
>>> kenny = Dog()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    kenny = Dog()
TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'color'
>>> kenny = Dog('Kenny', 5, 'black')
>>> bingo = Dog('Bingo', 7, 'orange')
>>> 
>>> 
>>> kenny.name
'Kenny'
>>> bingo.name
'Bingo'
>>> kenny.age
5
>>> bingo.age
7
>>> class B:
	def __init__(self):
		pass

	
>>> B()
<__main__.B object at 0x7f9cf834ebe0>
>>> class B:
	def __init__(self):
		self.occupation = "lawyer"

		
>>> g = B()
>>> g.occupation
'lawyer'
>>> g
<__main__.B object at 0x7f9cf673cdf0>
>>> g.amount = 100
>>> g.amount
100
>>> f = B()
>>> f.occupation
'lawyer'
>>> f.amount
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    f.amount
AttributeError: 'B' object has no attribute 'amount'
>>> f.amount = 900
>>> f.amount
900
>>> class Dog:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
	def bark(self):
		print("woof woof")

		
>>> kenny.__init__()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    kenny.__init__()
TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'color'
>>> class Dog:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
	def bark(self, num):
		for i in range(num):
			print("woof woof")

			
>>> master = Dog('master', 4, 'blue')
>>> master.bark(4)
woof woof
woof woof
woof woof
woof woof
>>> master.bark(2)
woof woof
woof woof
>>> master
<__main__.Dog object at 0x7f9cf8496880>
>>> master.bark(2)
woof woof
woof woof
>>> class Dog:
	species = 'rot wiler'
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
	def bark(self, num):
		for i in range(num):
			print("woof woof")

			
>>> master = Dog('master', 4, 'blue')
>>> kenny = Dog('Kenny', 5, 'black')
>>> master.name
'master'
>>> kenny.name
'Kenny'
>>> kenny.species
'rot wiler'
>>> master.species
'rot wiler'
>>> class Student:
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course

		
>>> student1 = Student('Julius Daniel', 45, 400, '
		   
SyntaxError: EOL while scanning string literal
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> student2 = Student('Abodunde', 24, 300, 'medicine')
>>> 
>>> student1.name
'Julius Daniel'
>>> student2.name
'Abodunde'
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course

		
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> student2 = Student('Abodunde', 24, 300, 'medicine')
>>> student1.university
'University of Lagos'
>>> student2 = Student('Abodunde', 24, 300, 'medicine')
>>> student2.university
'University of Lagos'
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")

				
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> student1.register(5000)
registration successfull
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> student1.registered
False
>>> student1.register(5000)
registration successfull
>>> student1.registered
True
>>> student2 = Student('Abodunde', 24, 300, 'medicine')
>>> student2.registered
False
>>> student2.register(50)
Registration cost 5000 naira only!
>>> student2.register(5000)
registration successfull
>>> student2.register(5000)
You are already registered
>>> student1.register(5000)
You are already registered
>>> 
>>> 
>>> 
>>> student1
<__main__.Student object at 0x7f9cf8496b80>
>>> []
[]
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")
	def __str__(self):
		return f"Name: {self.name}\nLevel: {self.level}"

	
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> student1
<__main__.Student object at 0x7f9cf8496d30>
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")

				
>>> student1
<__main__.Student object at 0x7f9cf8496d30>
>>> print(student1)
Name: Julius Daniel
Level: 400
>>> 
========================================== RESTART: Shell =========================================
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")

				
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> print(student1)
<__main__.Student object at 0x7fe2852ec310>
>>> student1
<__main__.Student object at 0x7fe2852ec310>
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")

				
>>> class Student:
	university = "University of Lagos"
	def __init__(self, name, age, level, course):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")
	def __str__(self):
		return f"Name: {self.name}\nLevel: {self.level}"

	
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science')
>>> print(student1)
Name: Julius Daniel
Level: 400
>>> student2 = Student('Abodunde', 24, 300, 'medicine')
>>> print(student2)
Name: Abodunde
Level: 300
>>> class Student:
	
	def __init__(self, name, age, level, course, university):
		self.name = name
		self.age = age
		self.level = level
		self.course = course
		self.registered = False
		self.university = university
	def register(self, amount):
		if self.registered:
			print("You are already registered")
		else:
			if amount != 5000:
				print("Registration cost 5000 naira only!")
			else:
				self.registered = True
				print("registration successfull")
	def __str__(self):
		return f"Name: {self.name}\nLevel: {self.level}"

	
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science', 'University of Ilorin)
		   
SyntaxError: EOL while scanning string literal
>>> student1 = Student('Julius Daniel', 45, 400, 'computer science', 'University of Ilorin')
>>> student1.university
'University of Ilorin'
>>> student2 = Student('Abodunde', 24, 300, 'medicine', 'Lagos State University')
>>> student2.university
'Lagos State University'
>>> 