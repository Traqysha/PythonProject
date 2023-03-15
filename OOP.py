class Fruits:
    def __init__(self,type,color,price):
        self.mytype=type
        self.mycolor=color
        self.myprice=price

    def onyesha(self):
        print(self.mytype,self.mycolor,self.myprice)

# create an object
myobj= Fruits("Banana","Yellow",20)
myobj.onyesha()

myobj1= Fruits("Mango","Orange",50)
myobj1.onyesha()

myobj2= Fruits("Apple","Red",30)
myobj2.onyesha()

myobj3= Fruits("Grapes","Purple",250)
myobj3.onyesha()

class Employees:
    def __init__(self,name,salary):
        self.myname=name
        self.mysalary=salary

    def employ(self):
        print("Employee"+" "+ "is"+" "+ self.myname,"monthly salary is",self.mysalary)

employment= Employees("John",45700)
employment.employ()

employment2= Employees("Karen",54900)
employment2.employ()
