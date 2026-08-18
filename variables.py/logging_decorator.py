def logger(function):
    def wrapper(*args, **kwargs):
        print("function started")

        result = function(*args, **kwargs)

        print("function finished")

        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

result = multiply (4, 5)
print("result:", result)