##student_names = []
##
##while True:
##    name = input("Enter the name of the student (leave blank to end): ")
##
##    if name == '':
##        print(f"\nYou have entered the names of {len(student_names)} students\n")
##        break
##    student_names += [name]
##
##print("These are the names of  students currently in your class\n")


##for i in range(len(student_names)):
##    print(f"{i+1}. {student_names[i]}")





##student_names = ['jeremiah', 'joseph', 'charles', 'bitrus', 'olusola', 'david', 'sunny', 'daniel', 'chidi', 'williams', 'olumide', 'anthony']
##print(f"\nYou have entered the names of {len(student_names)} students\n")
##print("These are the names of  students currently in your class\n")
##
####for name in student_names:
####    print(name)
##
##for index, name in enumerate(student_names):
##    print(f"{index+1}. {name}")
##a = [int(x) for x in input().split()]
##num1 = list(map(int,input("enter: ").split()))
##print(num1)            
            


L=list(map(int,input("enter: ").split()))
print(L)
a = [int(x) for x in input("enter: ")]
print(a)


def retList():
    list = []
    for i in range(10,50, 10):
        list.append(i)
    return list
a = retList()
print(a)

def create_list():
    memo=[] 
    for i in range(int(input("Enter no: "))):
        x=int(input("enter no:" )) 
        memo.insert(i,x)
        i+=1
    return memo 

a = create_list()
print(a)
