"""
64. Take employees info (id,name, age, adress, sal, height, weight)
	a. Take id, provide employee information for that id.
	b. find out average salary.
	c. find out which age, address taking the heighest salary 
	d. find out every employee BMI value
	e. Finally find out the Organization overall BMI
"""
import sqlite3 as lite
con = lite.connect('assigndb')
cur = con.cursor()
while True:
    n=raw_input("a. empoinfo of givenid\nb.average salary\nc.find out which age, address\nd.every employee BMI value\ne.overall BMI\nf.quit")
    if n.lower()=='a':
        EMPID=input("Enter the employee id:")
        cur.execute("select * from employeeinfo2 where EMPID=?",(EMPID,))
        for i in cur:
            print i
    elif n.lower()=='b':
         cur.execute("select EMPSAL from employeeinfo2")
         list1=[]
         list2=[]
         for i in cur:
             list1.append(list(i))
         for i in list1:
             if type(i)==list:
                 for j in i:
                     list2.append(j)
             else:
                 list2.append(i)
         avgsal=sum(list2)/len(list2)
         print "Average sal of all employess:", avgsal
    elif n.lower()=='c':
        cur.execute("select EMPSAL from employeeinfo2")
        list1=[]
        list2=[]
        for i in cur:
            list1.append(list(i))
        for i in list1:
            if type(i)==list:
                for j in i:
                    list2.append(j)
            else:
                list2.append(i)
        maxsal=max(list2)
        cur.execute("select EMPAGE ,EMPADDRESS from employeeinfo2 where EMPSAL=?",(maxsal,))
        for i in cur:
            print "Age and address of employee:", i
    elif n.lower()=='d':
        EMPID=input("Enter the employee id:")
        cur.execute("select EMPHEIGHT,EMPWEIGHT from employeeinfo2 where EMPID=?",(EMPID,))
        for i in cur:
            a=i
        hinm=a[1]/100
        bmi=a[0]/(hinm*hinm)
        print "BMI of selected employee is:",bmi
    elif n.lower()=='e':
        cur.execute("select EMPHEIGHT,EMPWEIGHT from employeeinfo2")
        list1=[]
        for i in cur:
            hinm=i[1]/100
            bmi=i[0]/(hinm*hinm)
            list1.append(bmi)
        print "sum of overall all  bmi:",sum(list1)
    else:
        print "quit"
        break
        
