Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> details = {'name': 'Charles', 'age': 30, 'occupation': 'trader'}
>>> details['name']
'Charles'
>>> deatails['age']
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    deatails['age']
NameError: name 'deatails' is not defined
>>> details['age']
30
>>> customers = { 1: details, 2: {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}, 3: {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}, 4: { 'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}, 5: { 'name': 'sunny', 'age': 34, 'occupation': 'tailor'}, 6: { 'name': 'dotun', 'age': 34, 'occupation': 'tailor'}, 7 : { 'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}, 8: { 'name': 'David', 'age': 34, 'occupation': 'tailor'}, 9: { 'name': 'Nathan', 'age': 19, 'occupation': 'student'}, 10: { 'name': 'Jason', 'age': 19, 'occupation': 'student'}}
>>> 
>>> customers
{1: {'name': 'Charles', 'age': 30, 'occupation': 'trader'}, 2: {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}, 3: {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}, 4: {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}, 5: {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}, 6: {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}, 7: {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}, 8: {'name': 'David', 'age': 34, 'occupation': 'tailor'}, 9: {'name': 'Nathan', 'age': 19, 'occupation': 'student'}, 10: {'name': 'Jason', 'age': 19, 'occupation': 'student'}}
>>> import pprint
>>> pprint.pprint(customers)
{1: {'age': 30, 'name': 'Charles', 'occupation': 'trader'},
 2: {'age': 25, 'name': 'Micahel', 'occupation': 'footballer'},
 3: {'age': 27, 'name': 'Alisson', 'occupation': 'footballer'},
 4: {'age': 23, 'name': 'Johnson', 'occupation': 'doctor'},
 5: {'age': 34, 'name': 'sunny', 'occupation': 'tailor'},
 6: {'age': 34, 'name': 'dotun', 'occupation': 'tailor'},
 7: {'age': 34, 'name': 'Olamide', 'occupation': 'tailor'},
 8: {'age': 34, 'name': 'David', 'occupation': 'tailor'},
 9: {'age': 19, 'name': 'Nathan', 'occupation': 'student'},
 10: {'age': 19, 'name': 'Jason', 'occupation': 'student'}}
>>> print(customers)
{1: {'name': 'Charles', 'age': 30, 'occupation': 'trader'}, 2: {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}, 3: {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}, 4: {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}, 5: {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}, 6: {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}, 7: {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}, 8: {'name': 'David', 'age': 34, 'occupation': 'tailor'}, 9: {'name': 'Nathan', 'age': 19, 'occupation': 'student'}, 10: {'name': 'Jason', 'age': 19, 'occupation': 'student'}}
>>> pprint.pprint(customers)
{1: {'age': 30, 'name': 'Charles', 'occupation': 'trader'},
 2: {'age': 25, 'name': 'Micahel', 'occupation': 'footballer'},
 3: {'age': 27, 'name': 'Alisson', 'occupation': 'footballer'},
 4: {'age': 23, 'name': 'Johnson', 'occupation': 'doctor'},
 5: {'age': 34, 'name': 'sunny', 'occupation': 'tailor'},
 6: {'age': 34, 'name': 'dotun', 'occupation': 'tailor'},
 7: {'age': 34, 'name': 'Olamide', 'occupation': 'tailor'},
 8: {'age': 34, 'name': 'David', 'occupation': 'tailor'},
 9: {'age': 19, 'name': 'Nathan', 'occupation': 'student'},
 10: {'age': 19, 'name': 'Jason', 'occupation': 'student'}}
>>> customers[1]
{'name': 'Charles', 'age': 30, 'occupation': 'trader'}
>>> customers[1]['age']
30
>>> cutomers.keys()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    cutomers.keys()
NameError: name 'cutomers' is not defined
>>> customers.keys()
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
\
>>> for i in customers:
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> customers.values()
dict_values([{'name': 'Charles', 'age': 30, 'occupation': 'trader'}, {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}, {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}, {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}, {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}, {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}, {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}, {'name': 'David', 'age': 34, 'occupation': 'tailor'}, {'name': 'Nathan', 'age': 19, 'occupation': 'student'}, {'name': 'Jason', 'age': 19, 'occupation': 'student'}])
>>> for x in customers.values():
	print(x)

	
{'name': 'Charles', 'age': 30, 'occupation': 'trader'}
{'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}
{'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}
{'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}
{'name': 'sunny', 'age': 34, 'occupation': 'tailor'}
{'name': 'dotun', 'age': 34, 'occupation': 'tailor'}
{'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}
{'name': 'David', 'age': 34, 'occupation': 'tailor'}
{'name': 'Nathan', 'age': 19, 'occupation': 'student'}
{'name': 'Jason', 'age': 19, 'occupation': 'student'}
>>> customers.values()
dict_values([{'name': 'Charles', 'age': 30, 'occupation': 'trader'}, {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}, {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}, {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}, {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}, {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}, {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}, {'name': 'David', 'age': 34, 'occupation': 'tailor'}, {'name': 'Nathan', 'age': 19, 'occupation': 'student'}, {'name': 'Jason', 'age': 19, 'occupation': 'student'}])
>>> customers.items()
dict_items([(1, {'name': 'Charles', 'age': 30, 'occupation': 'trader'}), (2, {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}), (3, {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}), (4, {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}), (5, {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}), (6, {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}), (7, {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}), (8, {'name': 'David', 'age': 34, 'occupation': 'tailor'}), (9, {'name': 'Nathan', 'age': 19, 'occupation': 'student'}), (10, {'name': 'Jason', 'age': 19, 'occupation': 'student'})])
>>> from pprint import pprint
>>> pprint(customers.items())
dict_items([(1, {'name': 'Charles', 'age': 30, 'occupation': 'trader'}), (2, {'name': 'Micahel', 'age': 25, 'occupation': 'footballer'}), (3, {'name': 'Alisson', 'age': 27, 'occupation': 'footballer'}), (4, {'name': 'Johnson', 'age': 23, 'occupation': 'doctor'}), (5, {'name': 'sunny', 'age': 34, 'occupation': 'tailor'}), (6, {'name': 'dotun', 'age': 34, 'occupation': 'tailor'}), (7, {'name': 'Olamide', 'age': 34, 'occupation': 'tailor'}), (8, {'name': 'David', 'age': 34, 'occupation': 'tailor'}), (9, {'name': 'Nathan', 'age': 19, 'occupation': 'student'}), (10, {'name': 'Jason', 'age': 19, 'occupation': 'student'})])
>>> pprint(list(customers.items()))
[(1, {'age': 30, 'name': 'Charles', 'occupation': 'trader'}),
 (2, {'age': 25, 'name': 'Micahel', 'occupation': 'footballer'}),
 (3, {'age': 27, 'name': 'Alisson', 'occupation': 'footballer'}),
 (4, {'age': 23, 'name': 'Johnson', 'occupation': 'doctor'}),
 (5, {'age': 34, 'name': 'sunny', 'occupation': 'tailor'}),
 (6, {'age': 34, 'name': 'dotun', 'occupation': 'tailor'}),
 (7, {'age': 34, 'name': 'Olamide', 'occupation': 'tailor'}),
 (8, {'age': 34, 'name': 'David', 'occupation': 'tailor'}),
 (9, {'age': 19, 'name': 'Nathan', 'occupation': 'student'}),
 (10, {'age': 19, 'name': 'Jason', 'occupation': 'student'})]
>>> 
>>> 
>>> 
>>> 1 in customers.keys()
True
>>> 11 in customers.keys()
False
>>> customers[11]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    customers[11]
KeyError: 11
>>> customers.get(1)
{'name': 'Charles', 'age': 30, 'occupation': 'trader'}
>>> customers[1]
{'name': 'Charles', 'age': 30, 'occupation': 'trader'}
>>> customers[11]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    customers[11]
KeyError: 11
>>> customers.get(11)
>>> print(customers.get(12))
None
>>> if customers.get(13) is None:
	print("does not exists")

	
does not exists
>>> if customers[13] is None:
	print("does not exists")

	
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    if customers[13] is None:
KeyError: 13
>>> if customers.get(13) is None:
	print("does not exists")

	
does not exists
>>> customers.get(1, "DOES NOT EXISTS")
{'name': 'Charles', 'age': 30, 'occupation': 'trader'}
>>> customers.get(8, "DOES NOT EXISTS")
{'name': 'David', 'age': 34, 'occupation': 'tailor'}
>>> customers.get(15, "DOES NOT EXISTS")
'DOES NOT EXISTS'
>>> customers.get(15, [])
[]
>>> 