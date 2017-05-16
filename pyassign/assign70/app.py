"""
70. Write a class(DB) program to create a table, insert values, update values, delete values of the table. 
All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).
In app.py create instance of the DB class and call all the methods by passing some data.
"""
import dboperations

dbobj=dboperations.database_op()
con,cur=dbobj.connect()
dbobj.db_create_op(cur)
dbobj.db_insert_op(1,'xyz','xyz@123',cur,con)
dbobj.db_update_op(1,'abc',cur,con)
dbobj.db_delete_op(1,cur,con)





