class student:
    def __init__(self,name):
        self.name = name
    def method1(self):
        print("student name is", self.name)
s1=student("nikhil")
s1.method1()
s2=student("liya")
s2.method1() 