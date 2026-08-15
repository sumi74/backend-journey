number = [1, 2, 3, 4, 5]
squares = [number * number for number in number]
print(squares)

even_numbers = [number for number in number if number % 2 ==0]
print(even_numbers)

odd_numbers = [number for number in number if number % 2 != 0]
print(odd_numbers)
# 
number =[1, 2, 3, 4, 5]
result = ["even" if number % 2 ==0 else "odd" for number in number]
print(result)
#
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big_number = [number for number in number if number > 5]
print(big_number)
#
names = ["ali", "sumi", "amina", "ahmed"]
long_names = [name for name in names if len(name) > 4]
print(long_names)
