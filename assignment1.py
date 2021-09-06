while True:
    length = float(input("enter the length: "))
    breadth = float(input("enter the breadth: "))
    height = float(input("enter the height: "))

    volume = length * breadth * height

    print("volume: ", volume, "cm")
    print("Do you want to perform another computation?")

    while True:
        enter = input("Enter if you want to continue or not: ")
        if enter == "yes" or enter == "y":
            break

        if enter != "no" or enter != "n":
            break

    if enter == "no" or enter == 'n':
        break

print("Done and quit")


