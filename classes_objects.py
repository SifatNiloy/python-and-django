class MyClass:
    x=5

p1= MyClass()
# print(p1.x)


class Student:
    roll=""
    gpa=""

    def display(self):
        print(f"Roll: {self.roll}, gpa:{self.gpa}")

Rahim= Student()
Rahim.roll=101
Rahim.gpa=4.0
print(f"Roll: {Rahim.roll}, gpa:{Rahim.gpa}")

Karim= Student()
Karim.roll = 102
Karim.gpa = 3.9
print(f"Roll: {Karim.roll}, gpa:{Karim.gpa}")
