class s:
    def __init__(self):
        self.USN=None
        self.Name=None
        self.Marks=[]
        self.precentage=None
        self.Grade=None
    def inPut(self):
         self.Name=input("enter name:")
         self.USN=(input("enter USN:"))
         for i in range(0,5):
            marks=int(input(f"Enter marks for sub {i+1}: "))
            self.Marks.append(marks)
         self.pre()
    def pre(self):
        sum=0
        for i in self.Marks:
            sum+=i
        self.percentage=(sum/500)*100
        self.m=self.percentage
        self.grade()
    def grade(self):
        p=self.m
        if p >= 90:
            self.Grade="A"
        elif p>=80:
            self.Grade="B"
        elif p>=70:
            self.Grade="C"
        elif p>=60:
            self.Grade="D"
        else:
            self.Grade="Fail"
        self.details()
    def details(self):
        print("-------------------------------------------------------------")
        print("Name:",self.Name.capitalize())
        print("USN:",self.USN.upper())
        for i in range(0,5):
            print(f"Marks of {i+1} is:",self.Marks[i])
        print(round(self.percentage,2))
        print(self.Grade)
        print("-------------------------------------------------------------")     
o=0
n=int(input("Enter No of Students:"))
for i in range(n):
    o+=1
    su=str(o)
    su=s()
    print(f"Enter {i+1} students details of: ")
    su.inPut()
# Student.pre()
# Student.grade()
# Student.details()
