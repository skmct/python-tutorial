class school:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        
        print("student name",self.name)
    def show_age(self):
        print("student age",self.age)

s1=school("mohan",20)
s2=school("sohan",21)
s3=school("sandeep",19)
s4=school("lucky",30)
print(getattr(s1,'name'),':',getattr(s1,'age'))
setattr(s1,'age',21)
print(getattr(s1,'name'),':',getattr(s1,'age'))
print(hasattr(s1,'dob'))
print(s1.__dict__)
print(s1.__doc__)
print(s1.__module__))
