def add(a, b):
    return a + b
result = add(5, 3)
print(result)

# 
def multiply(a, b):
    return a * b

result = multiply(6, 4)
print(result)
#
def subtract(a, b):
    return a - b

result = subtract(10, 3)
print(result)
#
def divide(a, b):
    return a / b

result = divide(20, 5)
print(result)
#
def square(a):
    return a * a

result = square(6)
print(result)

#check_number(number)

def check_number(number):
    if number > 0:
        print("positive")
    else:
        print("not postive") 
check_number(5)
#
def check_number(number):
    if number > 0:
        print("positive")
    else:
        print("not postive")
check_number(-5)

#
def greet(name):
    print("hello", name)

greet("ali")
greet("amina")
#
def double(number):
    return number * 2

result = double(5)
print(result)
#
def greet(name):
    return "hello " + name
result = greet("ali")
print(result)
#
def greet_user(name):
    return "welocme " + name
result = greet_user("amina")
print(result)

#
def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

result = is_even(10)
print(result)
#
def is_even(number):
    if number % 2 ==0:
       return "even"
    else:
        return "odd"

result = is_even(7)
print(result)


