Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> foods  = ['rice', 'beans', 'eggs', 'salad', 56, 70, ['dog', 'cat']]
>>> len(foods)
7
>>> foods
['rice', 'beans', 'eggs', 'salad', 56, 70, ['dog', 'cat']]
>>> foods[6]
['dog', 'cat']
>>> foods[0]
'rice'
>>> foods[1]
'beans'
>>> food[0] + ' and ' + food[1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    food[0] + ' and ' + food[1]
NameError: name 'food' is not defined
>>> foods[0] + ' and ' + foods[1]
'rice and beans'
>>> foods[-1]
['dog', 'cat']
>>> foods[-5]
'eggs'
>>> foods[1:4]
['beans', 'eggs', 'salad']
>>> foods[:6:2]
['rice', 'eggs', 56]
>>> foods[:]
['rice', 'beans', 'eggs', 'salad', 56, 70, ['dog', 'cat']]
>>> foods[::-1]
[['dog', 'cat'], 70, 56, 'salad', 'eggs', 'beans', 'rice']
>>> foods[6] = 'bread'
>>> foods
['rice', 'beans', 'eggs', 'salad', 56, 70, 'bread']
>>> foods[1] = 'meat'
>>> foods
['rice', 'meat', 'eggs', 'salad', 56, 70, 'bread']
>>> foods + ['fish', 'swallow']
['rice', 'meat', 'eggs', 'salad', 56, 70, 'bread', 'fish', 'swallow']
>>> foods*2
['rice', 'meat', 'eggs', 'salad', 56, 70, 'bread', 'rice', 'meat', 'eggs', 'salad', 56, 70, 'bread']
>>> foods
['rice', 'meat', 'eggs', 'salad', 56, 70, 'bread']
>>> del foods[1]
>>> foods
['rice', 'eggs', 'salad', 56, 70, 'bread']
>>> 
>>> name = input()

>>> name
''
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================
Enter the name of the student (leave blank to end): james
Enter the name of the student (leave blank to end): daniel
Enter the name of the student (leave blank to end): tolu
Enter the name of the student (leave blank to end): ezekiel
Enter the name of the student (leave blank to end): julius
Enter the name of the student (leave blank to end): stephen
Enter the name of the student (leave blank to end): michael
Enter the name of the student (leave blank to end): victory
Enter the name of the student (leave blank to end): confession
Enter the name of the student (leave blank to end): miracle
Enter the name of the student (leave blank to end): progress
Enter the name of the student (leave blank to end): chinedu
Enter the name of the student (leave blank to end): precious
Enter the name of the student (leave blank to end): vivian
Enter the name of the student (leave blank to end): 
you have entered the names of 14 students
Students: ['james', 'daniel', 'tolu', 'ezekiel', 'julius', 'stephen', 'michael', 'victory', 'confession', 'miracle', 'progress', 'chinedu', 'precious', 'vivian']
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================
Enter the name of the student (leave blank to end): gabriel
Enter the name of the student (leave blank to end): james
Enter the name of the student (leave blank to end): emeka
Enter the name of the student (leave blank to end): chinedu
Enter the name of the student (leave blank to end): 

You have entered the names of 4 students
Students: ['gabriel', 'james', 'emeka', 'chinedu']
>>> list(range(4))
[0, 1, 2, 3]
>>> len(foods)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    len(foods)
NameError: name 'foods' is not defined
>>> student_names
['gabriel', 'james', 'emeka', 'chinedu']
>>> len(student_names)
4
>>> range(4)
range(0, 4)
>>> range(len(student_names))
range(0, 4)
>>> student_names + ['mayor', 'emmanuel']
['gabriel', 'james', 'emeka', 'chinedu', 'mayor', 'emmanuel']
>>> student_names = student_names + ['mayor', 'emmanuel']
>>> student_names
['gabriel', 'james', 'emeka', 'chinedu', 'mayor', 'emmanuel']
>>> range(len(student_names))
range(0, 6)
>>> del student_names[-1:-3]
>>> student_names
['gabriel', 'james', 'emeka', 'chinedu', 'mayor', 'emmanuel']
>>> del student_names[-1]
>>> del student_names[-2]
>>> student_names
['gabriel', 'james', 'emeka', 'mayor']
>>> print(student_names[0])
gabriel
>>> print(student_names[1])
james
>>> print(student_names[2])
emeka
>>> print(student_names[3])
mayor
>>> range(0, 4)
range(0, 4)
>>> range(4)
range(0, 4)
>>> len(student_names)
4
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================
Enter the name of the student (leave blank to end): jeremiah
Enter the name of the student (leave blank to end): joseph
Enter the name of the student (leave blank to end): charles
Enter the name of the student (leave blank to end): bitrus
Enter the name of the student (leave blank to end): olusola
Enter the name of the student (leave blank to end): david
Enter the name of the student (leave blank to end): sunny
Enter the name of the student (leave blank to end): daniel
Enter the name of the student (leave blank to end): chidi
Enter the name of the student (leave blank to end): williams
Enter the name of the student (leave blank to end): olumide
Enter the name of the student (leave blank to end): anthony
Enter the name of the student (leave blank to end): mena
Enter the name of the student (leave blank to end): victory
Enter the name of the student (leave blank to end): ikechukwu
Enter the name of the student (leave blank to end): alfred
Enter the name of the student (leave blank to end): 

You have entered the names of 16 students

These are the names of  students currently in your class
jeremiah
joseph
charles
bitrus
olusola
david
sunny
daniel
chidi
williams
olumide
anthony
mena
victory
ikechukwu
alfred
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================
Enter the name of the student (leave blank to end): jeremiah
Enter the name of the student (leave blank to end): joseph
Enter the name of the student (leave blank to end): charles
Enter the name of the student (leave blank to end): bitrus
Enter the name of the student (leave blank to end): olusola
Enter the name of the student (leave blank to end): david
Enter the name of the student (leave blank to end): sunny
Enter the name of the student (leave blank to end): daniel
Enter the name of the student (leave blank to end): chidi
Enter the name of the student (leave blank to end): williams
Enter the name of the student (leave blank to end): olumide
Enter the name of the student (leave blank to end): anthony
Enter the name of the student (leave blank to end): 

You have entered the names of 12 students

These are the names of  students currently in your class

1. jeremiah
2. joseph
3. charles
4. bitrus
5. olusola
6. david
7. sunny
8. daniel
9. chidi
10. williams
11. olumide
12. anthony
>>> student_names
['jeremiah', 'joseph', 'charles', 'bitrus', 'olusola', 'david', 'sunny', 'daniel', 'chidi', 'williams', 'olumide', 'anthony']
>>> 'joseph' in student_names
True
>>> 'charles' in student_names
True
>>> 'olivia' in student_names
False
>>> 'c' in 'chidiebere'
True
>>> 'f' in 'chidiebere'
False
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================

You have entered the names of 12 students

These are the names of  students currently in your class

jeremiah
joseph
charles
bitrus
olusola
david
sunny
daniel
chidi
williams
olumide
anthony
>>> a = 10
>>> b = 20
>>> a, b = [10, 20]
>>> a
10
>>> b
20
>>> a, b = [50, 70]
>>> a
50
>>> b
70
>>> a, b, c = [50, 70, 90]
>>> a
50
>>> b
70
>>> c
90
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================

You have entered the names of 12 students

These are the names of  students currently in your class

(0, 'jeremiah')
(1, 'joseph')
(2, 'charles')
(3, 'bitrus')
(4, 'olusola')
(5, 'david')
(6, 'sunny')
(7, 'daniel')
(8, 'chidi')
(9, 'williams')
(10, 'olumide')
(11, 'anthony')
>>> names = ('daniel', 'micheal')
>>> names[0]
'daniel'
>>> names[1]
'micheal'
>>> names[0] = 'bolton'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    names[0] = 'bolton'
TypeError: 'tuple' object does not support item assignment
>>> a, b, c = (20, 50, 63)
>>> a
20
>>> b
50
>>> c
63
>>> 50, 70
(50, 70)
>>> a, b, c = 20, 50, 89
>>> a, b = 20, 50, 89
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a, b = 20, 50, 89
ValueError: too many values to unpack (expected 2)
>>> a, b, c = 20, 50
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a, b, c = 20, 50
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
=================== RESTART: /Users/gnc/Documents/python_bootcamp_28_aug.py ===================

You have entered the names of 12 students

These are the names of  students currently in your class

1. jeremiah
2. joseph
3. charles
4. bitrus
5. olusola
6. david
7. sunny
8. daniel
9. chidi
10. williams
11. olumide
12. anthony
>>> import random
>>> import math
>>> import kshd
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    import kshd
ModuleNotFoundError: No module named 'kshd'
>>> math.cos(60)
-0.9524129804151563
>>> math.cos(30)
0.15425144988758405
>>> random.randrange(9)
2
>>> random.randrange(9)
0
>>> random.randrange(9)
7
>>> random.randrange(9)
7
>>> random.shuffle(student_names)
>>> student_names
['bitrus', 'joseph', 'chidi', 'williams', 'olumide', 'david', 'olusola', 'daniel', 'anthony', 'charles', 'jeremiah', 'sunny']
>>> random.choice(student_names)
'chidi'
>>> student_names
['bitrus', 'joseph', 'chidi', 'williams', 'olumide', 'david', 'olusola', 'daniel', 'anthony', 'charles', 'jeremiah', 'sunny']
>>> student_names.index('chidi')
2
>>> student_names.index('david')
5
>>> student_names.index('vivian')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    student_names.index('vivian')
ValueError: 'vivian' is not in list
>>> scores = [100, 45, 78, 98]
>>> scores[0]
100
>>> scores = scores + [67]
>>> scores
[100, 45, 78, 98, 67]
>>> scores += [88, 45]
>>> scores
[100, 45, 78, 98, 67, 88, 45]
>>> scores.append(57)
>>> scores
[100, 45, 78, 98, 67, 88, 45, 57]
>>> scores.append(30)
>>> scores
[100, 45, 78, 98, 67, 88, 45, 57, 30]
>>> scores.insert(1, 87)
>>> scores
[100, 87, 45, 78, 98, 67, 88, 45, 57, 30]
>>> scores.insert(0, 83)
>>> scores
[83, 100, 87, 45, 78, 98, 67, 88, 45, 57, 30]
>>> scores.insert(4, 78)
>>> scores
[83, 100, 87, 45, 78, 78, 98, 67, 88, 45, 57, 30]
>>> del scores[2]
>>> [83, 100, 87, 45, 78, 78, 98, 67, 88, 45, 57, 30]
[83, 100, 87, 45, 78, 78, 98, 67, 88, 45, 57, 30]
>>> del scores[1]
>>> scores
[83, 45, 78, 78, 98, 67, 88, 45, 57, 30]
>>> scores.remove(78)
>>> scores
[83, 45, 78, 98, 67, 88, 45, 57, 30]
>>> scores.remove(78)
>>> scores
[83, 45, 98, 67, 88, 45, 57, 30]
>>> scores.remove(110)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    scores.remove(110)
ValueError: list.remove(x): x not in list
>>> scores.sort()
>>> scores
[30, 45, 45, 57, 67, 83, 88, 98]
>>> scores.sort(reverse=True)
>>> scores
[98, 88, 83, 67, 57, 45, 45, 30]
>>> 