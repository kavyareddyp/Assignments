"""
71.write a program to do registration.Write a methods in a class DB to open database connection and insert details in to database table. 
Write a Model parent class and implement a create method. Call a database insert method into the create  method. 
Write child class person for Model and override method create method and call the parent(Model) class create method in the child(person) 
create an instance of person class and call the create method.
"""

import sqlite3

class database(object):
    def connect(self,database_name):
        self.database_name=database_name
        self.con = sqlite3.connect(self.database_name)
        #self.cur=self.con.cursor()
        print 'conection sunccessfull'
        return self.con
    @staticmethod
    def insertdata(con,name,age,sal):
        a=(name,age,sal)
        con.execute("insert into empinfotable values(?,?,?)",a)
        con.commit()
class Method(database):
    def create_table(self,database_name,name,age,sal):
        con=self.connect(database_name)
        table_create="create table empinfotable(name varchar,age INT,sal INT )" 
        con.execute(table_create)
        print "table created"
        database.insertdata(con,name,age,sal)
        print "inserted data sucesfully"
class Person(Method):
    def creat_table(self,database_name,name,age,sal):
        super(cls,self).create_table(database_name,name,age,sal)
        
pobj=Person()
pobj.create_table("nexii","kavya","23",10000)

