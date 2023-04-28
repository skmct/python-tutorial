class Student:
    count=0
    def __init__(self):
        Student.count=Student.count + 1
        print("hello")
    def sum(self):
        print("sum wala hello")
s1=Student()
s2=Student()
s3=Student()

print("the number of student:",Student.count)