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
s3.show()
s3.show_age()
s2.show()
s5=school("local",20)
s5.show()        
