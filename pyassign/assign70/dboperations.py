"""
70. Write a class(DB) program to create a table, insert values, update values, delete values of the table. 
All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).
In app.py create instance of the DB class and call all the methods by passing some data.
"""

import sqlite3 as lite
"""
To create a db and estabblish the connection to db
"""
class database_op:
    def connect(self):
        con = lite.connect('assigndb')
        cur = con.cursor()
        return con,cur
    def db_create_op(self,cur):
        cur.execute("CREATE TABLE userinfo(USERID INT, NAME TEXT, PASSWD VARCHAR(50))")
        print "Database  created successfully"
    def db_insert_op(self,userid,name,passwd,cur,con):
        a=(userid,name,passwd)
        cur.execute("Insert into userinfo values(?,?,?)",a)
        con.commit()
        print "Inserted values succesfully"
    def db_update_op(self,userid,name,cur,con):
        cur.execute("update userinfo set name=? where userid=?",(name,userid))
        con.commit()
        print "Update values succesfully"
    def db_delete_op(self,userid,cur,con):
        cur.execute("delete from userinfo where userid=?",(userid,))
        con.commit()
        print "Deleted values successfully"

        






