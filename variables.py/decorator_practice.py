def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("something is happening before the function.")

        function(*args, **kwargs)

        print("something is happening after the function.")

    return wrapper



@my_decorator
def greet(name):
    print("hello", name)
    
greet("sumaya")

@my_decorator
def add(a, b):
    print(a + b)

add(5, 10)

@my_decorator
def introduce(name, role):
    print("my name is", name)
    print("i am a", role)

introduce(name="sumaya", role="backend developer")