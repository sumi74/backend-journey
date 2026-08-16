try:
    number = int(input("enter a number"))
    print(10 / number)

except ValueError:
     print("please enter a number.")

except ZeroDivisionError:
     print("you cannot divide by zero.")

else:
     print("the calculation worked successfully.")

finally:
     print("program finished.")
     