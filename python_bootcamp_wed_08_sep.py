Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in 'amen':
	print(i)

	
a
m
e
n
>>> [12, 45]
[12, 45]
>>> 
>>> 
>>> new = dict()
>>> new
{}
>>> dict = 'asdbfkjfa'
>>> dict
'asdbfkjfa'
>>> 
================================ RESTART: Shell ================================
>>> name = ['daniel', 'ebuka', 'sunny', 'dotun']
>>> age = [21, 19, 21, 19]
>>> 
>>> len(name)
4
>>> len(age)
4
>>> for i in range(len(age)):
	print(name[i], age[i])

	
daniel 21
ebuka 19
sunny 21
dotun 19
>>> 
>>> 
>>> for i in  zip(name, age):
	print(i)

	
('daniel', 21)
('ebuka', 19)
('sunny', 21)
('dotun', 19)
>>> 
>>> for n, a in zip(name, age):
	print(n, a)

	
daniel 21
ebuka 19
sunny 21
dotun 19
>>> def divideby2(num):
	if num == 1:
		return
	print(num // 2)
	divideby2(num//2)

	
>>> divideby2(800)
400
200
100
50
25
12
6
3
1
>>> divideby2(10)
5
2
1
>>> sqr = lambda x: x * x
>>> sqr(3)
9
>>> age
[21, 19, 21, 19]
>>> for i in age:
	new_list = []
	new_list.append(sqr(i))
	return new_list
SyntaxError: 'return' outside function
>>> for i in age:
	new_list = []
	new_list.append(sqr(i))

	
>>> new_list
[361]
>>> age
[21, 19, 21, 19]
>>> for i in age:
	print(sqr(i))

	
441
361
441
361
>>> new_list = []
>>> for i in age:
	new_list.append(sqr(i))

	
>>> new_list
[441, 361, 441, 361]
>>> 21 * 21
441
>>> 19 * 19
361
>>> map(sqr, age)
<map object at 0x7f9f582ec580>
>>> list(map(sqr, age))
[441, 361, 441, 361]
>>> age = list(map(sqr, age))
>>> age
[441, 361, 441, 361]
>>> age = list(map(sqr, age))
>>> age
[194481, 130321, 194481, 130321]
>>> age = list(map(sqr, age))
>>> age
[37822859361, 16983563041, 37822859361, 16983563041]
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
>>> new_list = []
>>> for i in range(1, 8):
	new_list.append(i*i)

	
>>> new_list
[1, 4, 9, 16, 25, 36, 49]
>>> [i*i for i in range(1, 8)]
[1, 4, 9, 16, 25, 36, 49]
>>> [i for i in range(1, 8)]
[1, 2, 3, 4, 5, 6, 7]
>>> [i*i for i in range(1, 8)]
[1, 4, 9, 16, 25, 36, 49]
>>> 
>>> new_list = []
>>> for i in range(1, 8):
	new_list.append(i*i)

	
>>> new_list
[1, 4, 9, 16, 25, 36, 49]
>>> [i*i for i in range(1, 8)]
[1, 4, 9, 16, 25, 36, 49]
>>> from functools import reduce
>>> reduce(lambda a, b: a + b, new_list)
140
>>> new_list
[1, 4, 9, 16, 25, 36, 49]
>>> reduce(lambda a, b: a + b, new_list)
140
>>> total = 0
>>> for i in new_list:
	total += i

	
>>> total
140
>>> def sum_list(numbers):
	total = 0
	for i in numbers:
		total += i
	return total

>>> sum_list(new_list)
140
>>> def addTwo(a, b):
	return a + b

>>> reduce(addtwo, new_list)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    reduce(addtwo, new_list)
NameError: name 'addtwo' is not defined
>>> reduce(addTwo, new_list)
140
>>> print('ree', 't erhher', 9, [90, 80])
ree t erhher 9 [90, 80]
>>> def mySum(*numbers):
	total = 0
	for i in numbers:
		total += i
	return total

>>> mySum(1,2,4,5,6,0)
18
>>> mySum(12, 34)
46
>>> def details(**kwargs):
	for key, value in kwargs.items():
		print(key, value)

		
>>> details(first="mabel", surname="seyi", age=19, class_= 100)
first mabel
surname seyi
age 19
class_ 100
>>> def details(**kwargs):
	print(kwargs)

	
>>> details(first="mabel", surname="seyi", age=19, class_= 100)
{'first': 'mabel', 'surname': 'seyi', 'age': 19, 'class_': 100}
>>> def mySum(*numbers):
	print(numbers)

	
>>> mySum(1,2,4,5,6,0)
(1, 2, 4, 5, 6, 0)
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 