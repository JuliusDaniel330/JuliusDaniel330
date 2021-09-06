# FUNCTION THAT DID NOT ASK THE USER FOR INPUT.

def return_day(day_num):
    if day_num < 1 or day_num > 7:
        return None
    elif day_num == 1:
        return "1 is Sunday"
    elif day_num == 2:
        return "2 is Monday"
    elif day_num == 3:
        return "3 is Tuesday"
    elif day_num == 4:
        return "4 is wednesday"
    elif day_num == 5:
        return "5 is Thursday"
    elif day_num == 6:
        return "6 is Friday"
    elif day_num == 7:
        return "7 is Saturday"


print(return_day(8))
print(return_day(2))
print(return_day(3))
print(return_day(0))

# FUNCTION CALLED IN A CODE THAT CONTINUOUSLY ASK THE USER IF THEY WANT TO CONTINUE OR NOT.


def return_day(day_num):
    if day_num < 1 or day_num > 7:
        return None
    elif day_num == 1:
        return "1 is Sunday"
    elif day_num == 2:
        return "2 is Monday"
    elif day_num == 3:
        return "3 is Tuesday"
    elif day_num == 4:
        return "4 is wednesday"
    elif day_num == 5:
        return "5 is Thursday"
    elif day_num == 6:
        return "6 is Friday"
    elif day_num == 7:
        return "7 is Saturday"


while True:
    day = int(input("Enter the day: "))
    print(return_day(day))
    enter = input("Enter if you want to continue or not: ")
    if enter == "yes" or enter == "y":
        continue
    else:
        break

return_day(4)



