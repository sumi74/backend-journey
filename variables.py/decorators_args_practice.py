def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("before the function")

        result = function(*args, **kwargs)

        print("after function")
        return result
    return wrapper

@my_decorator
def add (a, b):
    return a + b

result = add(5, 10)
print("result:", result)
