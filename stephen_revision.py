# This program takes in a parameter and returns the day of the week

def returnDay(day_week):
    if day_week ==1:
        return "Sunday"
    elif day_week == 2:
        return "Monday"
    elif day_week == 3:
        return "Tuesday"
    elif day_week ==4:
        return "Wednesday"
    elif day_week ==5:
        return "Thursday"
    elif day_week ==6:
        return "Friday"
    elif day_week == 7:
        return "Saturday"
    else:
        return "None"

print('This programme compute the day of the week')
while True:
        day = int(input("Enter the day: "))
        print(returnDay(day))    
        Response = input("enter 'yes' or 'y' to continue, enter 'no' or n to quit: ")

        if Response != "yes" and Response != "y":
            break
#day_week= int(input('what is the day of the week? '))
            



num = int(input('Size of elements : '))
arr = list()

for i in range(num) :
  ele  = int(input('Enter: '))
  arr.append(ele)

print(arr)
