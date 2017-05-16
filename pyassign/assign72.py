"""
72. create a user defined datatype, and provide functionalities of addition substraction and multiplication.
Create three instances(obj1,obj2,obj3) and print an output of obj1+obj2+obj3, obj1-obj2-obj3, obj1*obj2*obj3
"""
class userdeffun:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return userdeffun(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return userdeffun(x,y)
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return userdeffun(x,y)
P1=userdeffun(6,7)
P2=userdeffun(4,5)
P3=userdeffun(3,2)
print (P1+P2+P3)
print (P1-P2-P3)
print (P1*P2*P3)
