class student:

    def __init__(self, name, age, course,):
        self.name = name
        self.__age = age
        self.course = course

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("age must be greater than 0")

    def get_age(self):
        return self.__age 

    def set_get(self,new_age):
        self.__age = new_age


    def introduce(self):
        print(f"my name is {self.name}, i am {self.__age} years old, and i study {self.course}.")

    def study(self):
         print(f"{self.name} is studying backend development.")

    def change_course(self, new_course):
        self.course = new_course

student1 = student("ali", 20, "backend developer")
print(student1.name)
print(student1.course)
student1.introduce()

student2 = student("sundus", 21, "backend developer")

print(student2.name)
print(student2.course)
print(student2.get_age())
print(student2.get_age())

student2.set_age(22)
print(student2.get_age())

student2.introduce()
student2.study()


student2.change_course("django")
print(student2.course)
#
class developer(student):
    def code(self):
         print(f"{self.name} is writing python code.")

    def study(self):
        print(f"{self.name} is studying python for backend development")

    def deploy(self):
        print(f"{self.name} is deploying a backend application")
    
dev1 = developer("sundus", 21, "backend developer")

dev1.introduce()
dev1.study()
dev1.code()
dev1.deploy()

student2.set_age(-5)
print(student2.get_age())

#
class designer(student):
    def study(self):
        print(f"{self.name} is studying graphic design")

designer1 = designer("ali", 20, "graphic design")

designer1.study()
dev1.study()

class developer(student):
    def work(self):
        print(f"{self.name} is writing python code")

class designer(student):
    def work(self):
        print(f"{self.name} is designing graphics")

dev1 = developer("sundus", 21, "backend developer")
designer1 = designer("ali", 20, "graphic design")

dev1.work()
designer1.work()

class tester(student):
    def work(self):
        print(f"{self.name} is testing software")
tester1 = tester("ahmed", 22, "sotware testing")

dev1.work()
designer1.work()
tester1.work()

people = [dev1, designer1, tester1]

for person in people:
    person.work()

from abc import ABC, abstractmethod 
class animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class dog(animal):

    def sound(self):
        print("dog says: woof!")
dog = dog()
dog.sound()

class user: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"my name is {self.name}, l am {self.age} years old.")

user1 = user("sundus", 21)
user1.introduce()


class bank_account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"you balance is {self.__balance}")

account = bank_account(1000)
account.show_balance()
account.deposit(500)
account.show_balance()

class cat:
    def sound(self):
        print("cat says: meow!")

class dog:
    def sound(self):
        print("dog says: woof!")

animals = [ cat(), dog()]
for animal in animals:
    animal.sound()


class bankAcount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show_balance(self):
        print(f"{self.name}'s balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def  withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw: {amount}")
        else:
            print("insufficient balance")

    def transfer(self, other_account, amount):
            if amount <= self.__balance:
                self.__balance -= amount
                other_account.__balance += amount
                print(f"tranferred {amount}")
            else:
                print("insufficient balance")


account1 = bankAcount("sundus", 1000)
account1.show_balance()  
account1.deposit(500)
account1.show_balance()
account1.withdraw(300)
account1.show_balance()
account1.withdraw(2000)
account1.show_balance()

account2 = bankAcount("ali", 500)

account1.transfer(account2, 200)

account1.show_balance()
account2.show_balance()

class bankAcount2:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def show_balance(self):
        print(F"{self.name}, {self.__balance}")

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
           self.__balance -= amount
           print(f"withdraw: {amount}")
        else:
            print("insufficient balance")

    def transfer(self, other_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount
            print(f"tranferred {amount}")
        else:
            print("insufficient balance")


account1 = bankAcount2("sundus", 1000)
account1.show_balance()  
account1.deposit(300)
account1.show_balance()
account1.withdraw(200)
account1.show_balance()

account2 = bankAcount2("ali", 500)

account1.transfer(account2, 400)
account1.show_balance()
account2.show_balance()


        