"""
67. Collect emp information in a file Provide these operations.
    
    Menu:
     1. Get information information of an employee
     2. Modify employee information
     3. delete an employee information (Only status field change in the employee file)
     4. Add an employee.
"""

import csv
with open(r'D:\Assignments\assign67\empinfofile.csv','r') as ef:
    ufr=csv.reader(ef)
    list1=[]
    for row in ufr:
        list1.append(row)
while True:
    n=input("1.Get information of an employee\n2. Modify employee information\n3. delete an employee information\n4. Add an employee\n5.quit")
    if n==1:
        eid=raw_input("eneter the emp id:")
        for i in list1:
            if eid in i:
                print i
    elif n==2:
        eid=raw_input("enter the emp id:")
        mod_field = raw_input("Enter the field to be modified:1.name \n2salary\n3.status")
        if mod_field=="1":
            args = raw_input("Enter the  name:")
            for i in list1:
                if eid in i :
                    i[1]=args
        elif mod_field=="2":
            args = raw_input("Enter the salary:")
            for i in list1:
                if eid in i :
                    i[2]=args
        elif mod_field=="3":
            args = raw_input("Enter the status(Existing or NotExisting:")
            for i in list1:
                if eid in i :
                    i[3]=args
    elif n==3:
        eid=raw_input("enter the id of employee tobe deleted:")
        for i in list1:
                if eid in i :
                    args = raw_input("Enter the status(Existing or NotExisting:")
                    i[3]=args
    elif n==4:
        print "please enter the below details to add employee:"
        fields=[]
        eid=raw_input("Enter the id of employee:")
        name=raw_input("Enter the name of employee:")
        sal=raw_input("Enter thesal of employee:")
        status=raw_input("Enter the status whether (Existing or NotExisting):")
        a=(eid,name,sal,status)
        fields=list(a)
        update(fields)
        with open(r'D:\empinfofile.csv','a') as ef:
            writer = csv.writer(ef)
            writer.writerow(fields)
    else:
        print quit
        break
    
    
