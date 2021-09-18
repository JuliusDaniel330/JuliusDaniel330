# def my_function(values):
#     max = 0
#     for i in values:
#         if int(i) > max:
#             max = int(i)
#     print(max)
    



#name = "daniel"
#email="""
#hello {},
#how are you doing today?
#hope your night was cool?
#am happy seeing you today.

#"""    
#print(email.format(name))

# class Phone:


#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def call(self, phone_number):
#         print(f"{self.brand} is calling {phone_number}")



# iphone = Phone("iphone 7+", 300)
# samsung = Phone("samsung s20", 1400)

# print(iphone.brand)
# print(iphone.price)
# iphone.call("08138174405")


# print(samsung.brand)
# print(samsung.price)
# samsung.call("999")



# print("""this man here
# is a very bad man,
# and he is not only bad but
# also very wicked
# thank you.""")


#print('1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n')

# print("""
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.""")


# number = 0
# if number > 0:
#     print(f"number {number} is positive")
# elif number == 0:
#     print(number)
# else:
#     print(f"number {number} is negative")
    
    
    
    
# n = [2,4,6,8]
# res = 1
# for x in n[1:3]:
#     res = res * x
# print(res)
    

# weight = int(input())
# height = float(input())
# bmi = weight/(height*height)
# if (bmi < 18.5):
#     print("Underweight")
# elif(bmi >= 18.5 and bmi < 25):
#     print("Normal")
# elif(bmi > 25 and bmi < 30):
#     print("Overweight")
# elif(bmi > 30 and bmi > 35):
#     print("Obesity")
# else:
#     pass

    
# def func(x):
#     res = 0
#     for i in range(x):
#         print(i, res)
#         res = res + i
#     return res

# print(func(4)) 


# n = [2,4,6,8]
# res = 1
# for x in n[1:3]:
#     res = res * x
    
    
#print(res)

"""
class Dan:
    a = 20
    b = 30
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def clsMethd1(self): 
        ans = self.a + self.b
        print( ans) 
    def clsMethd2(self): 
        ans = self.c + self.d
        print( ans) 

Dan.a = 24 

o1 = Dan() 
print(o1.a)

o2 = Dan(13, 32)
print(o2.c)   
"""                  


#print(2 * (23 + 27 + 18))




import math
                                        
# We relay on our previous implementation for the variance
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])




    





