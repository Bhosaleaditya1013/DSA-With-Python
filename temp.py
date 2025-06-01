# Write a Python program to demonstrate single inheritance where a Person class is inherited by a Student class.

class Person:
    def show(self):
        print("This is person")
class Student:
    def display(self):
        print("This Is student")
        
class teacher(Person,Student):
    def profile(self):
        print("I am teachwr")
        
    
        
obj = teacher()
obj.display()
obj.show()
obj.profile()