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
