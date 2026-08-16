age = int(input("enter your age: "))

if age < 18:
    raise ValueError("you must be 18 or older.")

print("you can continue.")
