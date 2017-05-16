import sqlite3 as lite

con = lite.connect('assigndb')
cur = con.cursor()
cur.execute("CREATE TABLE employeeinfo2(EMPID VARCHAR, EMPNAME TEXT, EMPAGE INT ,EMPADDRESS TEXT,EMPSAL INT,EMPHEIGHT DOUBLE,EMPWEIGHT DOUBLE)")
n=input("Enter how many empolyess details you want enter into database:")
for i in range(n):
    EMPID=input("Enter a employee id:")
    EMPNAME=raw_input("Enter name of employee:")
    EMPAGE=input("Enter age of employye:")
    EMPADDRESS=raw_input("Enter address of employee:")
    EMPSAL=input("Enter sal details:")
    EMPHEIGHT=raw_input("Enter height of employee:")
    EMPWEIGHT=raw_input("Enter weight of employye:")
    a=(EMPID,EMPNAME,EMPAGE,EMPADDRESS,EMPSAL,EMPHEIGHT,EMPWEIGHT)
    cur.execute("Insert into employeeinfo2 values(?,?,?,?,?,?,?)",a)
con.commit()
print "Inserted values succesfully"
con.close()


