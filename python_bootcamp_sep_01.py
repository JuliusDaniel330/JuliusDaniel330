Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = ['fkjna', 3. ['lae']]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    d = ['fkjna', 3. ['lae']]
TypeError: 'float' object is not subscriptable
>>> d = ['fkjna', 3, ['lae']]
>>> d
['fkjna', 3, ['lae']]
>>> students_report = {'daniel': 95, 'victor': 83, 'tolu': 55, 'daniel': 100}
>>> scores = [80, 90, 70, 60]
>>> scores[0[]
       
SyntaxError: invalid syntax
>>> scores[0]
80
>>> scores[3]
60
>>> students_report = {'daniel': 95, 'victor': 83, 'tolu': 55, 'daniel': 100}
>>> students_report['daniel']
100
>>> students_report['daniel']
100
>>> students_report['victor']
83
>>> students_report['tolu']
55
>>> students_report['maryam']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    students_report['maryam']
KeyError: 'maryam'
>>> students = ['daniel', 'victor', 'tolu', 'ebuka']
>>> scores = [95, 83, 55, 100]
>>> students[0], scores[0]
('daniel', 95)
>>> animals = {'mammal': 'lion', 'reptiles': 'snakes'}
>>> beasts = {'reptiles': 'snakes', 'mammal': 'lion'}
>>> animals == beasts
True
>>> animals['mammal']
'lion'
>>> animals['reptiles']
'snakes'
>>> animals['mammal'] = 'tiger'
>>> animals
{'mammal': 'tiger', 'reptiles': 'snakes'}
>>> animals['birds'] = 'raven'
>>> animals
{'mammal': 'tiger', 'reptiles': 'snakes', 'birds': 'raven'}
>>> animals
{'mammal': 'tiger', 'reptiles': 'snakes', 'birds': 'raven'}
>>> animals['mammal'] = 'ram'
>>> animals
{'mammal': 'ram', 'reptiles': 'snakes', 'birds': 'raven'}
>>> animals['reptiles'] = 'lizard'
>>> animals
{'mammal': 'ram', 'reptiles': 'lizard', 'birds': 'raven'}
>>> animals['primates'] = 'Gorilla'
>>> animals
{'mammal': 'ram', 'reptiles': 'lizard', 'birds': 'raven', 'primates': 'Gorilla'}
>>> del animals['mammal']
>>> animals
{'reptiles': 'lizard', 'birds': 'raven', 'primates': 'Gorilla'}
>>> animals['mammals'] = ['lion', 'tiger', 'ram', 'humans', 'goat']
>>> animals
{'reptiles': 'lizard', 'birds': 'raven', 'primates': 'Gorilla', 'mammals': ['lion', 'tiger', 'ram', 'humans', 'goat']}
>>> school_staff = {'teaching': {'mathematics': 'segun', 'english': 'patience', 'chemistry': 'emeka'}, 'non_teaching': {'principal': 'Julius', 'vice_principal': 'Stephen'}}
>>> school_staff
{'teaching': {'mathematics': 'segun', 'english': 'patience', 'chemistry': 'emeka'}, 'non_teaching': {'principal': 'Julius', 'vice_principal': 'Stephen'}}
>>> school_staff['teaching']
{'mathematics': 'segun', 'english': 'patience', 'chemistry': 'emeka'}
>>> school_staff['non_teaching']
{'principal': 'Julius', 'vice_principal': 'Stephen'}
>>> school_staff['teaching']['mathematics']
'segun'
>>> animals
{'reptiles': 'lizard', 'birds': 'raven', 'primates': 'Gorilla', 'mammals': ['lion', 'tiger', 'ram', 'humans', 'goat']}
>>> beasts
{'reptiles': 'snakes', 'mammal': 'lion'}
>>> beasts.keys()
dict_keys(['reptiles', 'mammal'])
>>> for key in beasts.keys():
	print(key)

	
reptiles
mammal
>>> for i in beasts:
	print(i)

	
reptiles
mammal
>>> beasts.values()
dict_values(['snakes', 'lion'])
>>> for value in beasts.values():
	print(value)

	
snakes
lion
>>> beasts.items()
dict_items([('reptiles', 'snakes'), ('mammal', 'lion')])
>>> for elements in beasts.items():
	print(elements)

	
('reptiles', 'snakes')
('mammal', 'lion')
>>> a, b = 0. 70
SyntaxError: invalid syntax
>>> a, b = 0, 70
>>> a
0
>>> b
70
>>> a, b = ('to', 'go')
>>> a
'to'
>>> b
'go'
>>> for key, value in beasts.items():
	print("key:", key, "value:", value)

	
key: reptiles value: snakes
key: mammal value: lion
>>> animals
{'reptiles': 'lizard', 'birds': 'raven', 'primates': 'Gorilla', 'mammals': ['lion', 'tiger', 'ram', 'humans', 'goat']}
>>> school_staff
{'teaching': {'mathematics': 'segun', 'english': 'patience', 'chemistry': 'emeka'}, 'non_teaching': {'principal': 'Julius', 'vice_principal': 'Stephen'}}
>>> import pprint
>>> pprint.pprint(school_staff)
{'non_teaching': {'principal': 'Julius', 'vice_principal': 'Stephen'},
 'teaching': {'chemistry': 'emeka',
              'english': 'patience',
              'mathematics': 'segun'}}
>>> pprint.pprint(animals)
{'birds': 'raven',
 'mammals': ['lion', 'tiger', 'ram', 'humans', 'goat'],
 'primates': 'Gorilla',
 'reptiles': 'lizard'}
>>> 