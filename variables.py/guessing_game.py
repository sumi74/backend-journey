secret = 7
guess = 0

while guess != secret:
    guess = int(input("guess the number: "))

    if guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")

print("correct!")

#
for number in range(1, 6):
    print(number)
#
for number in range(1, 11):
    print(number)
# 
for number in range(10, 0, -1):
    print(number)
# 
for number in range(5, 0, -1):
    print("go!",  number)
#
for number in range(10, 0, -1):
    print("countdown:", number)
print("blast off")
# 
for number in range(10, 0, -1):
    print("countdown", number)

print("blast off!")
#
for number in range(2, 11, 2):
    print(number)
#
for number in range(1, 10, 2):
    print(number)
#
for number in range(5, 51, 5):
    print(number)
#
for number in range(20, 1, -2):
    print(number)
#
for number in range(1, 11):
   if number % 2 ==0:
    print(number)
     