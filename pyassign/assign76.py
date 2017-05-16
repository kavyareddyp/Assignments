"""
76.write a class program to demonstrate method overloading in python using below scenario:
write a class and constructor to create an instance like below
a.p1=person(id=1,name='aashok',age=23,sal=56787)
b.p2=person(id=2,age=24,adhar=23456)
c.p3=person(id=4,pan="brcp3456",sal=23,age=45)
make instance iterable and provide the operaton p1+p2
give your own defination for the operations
"""

class Person(object):
	def __init__(self,id1=0,name='',age=0,sal=0,pan=0,adhar=0):
		self.id1=id1
		self.name=name
		self.age=age
		self.sal=sal
		self.pan=pan
		self.adhar=adhar
	def get_info(self):
		return self.id1,self.name,self.age,self.sal,self.adhar,self.pan
	def __iter__(self):
		yield self.id1
		yield self.name
		yield self.age
		yield self.sal
		yield self.pan
		yield self.adhar
	def __add__(self1,self2):
		result={}
		result.update({'ID':self1.id1+self2.id1})
		result.update({'Name':self1.name+self2.name})
		result.update({'Salary':self1.sal+self2.sal})
		result.update({'adhar':self1.adhar+self2.adhar})
		result.update({'pan':self1.pan+self2.pan})
		result.update({'age':self1.age+self2.age})
		return result
p1=Person(id1=1,name="ashok",age=23,sal=56787)
p2=Person(id1=2,age=24,adhar=23456)
p3=Person(id1=4,pan="brcp3456",sal=23,age=45)
print "Iteration through p1 instance:"
for i in p1:
	print i
print "Addition of P1+P2:",p1+p2

