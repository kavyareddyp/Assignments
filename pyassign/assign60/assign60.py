"""
60. Show the below menu to the user:
     1. Add a row
     2. modify a row
     3. delete a row
     Go with one unique field in the file. And maintain that unique constraint in all file modifiction operations
     Use .CSV file for this program
"""
def add_row():
    f = open("data1.csv","a+")
    list1 =f.readlines()
    id1 =len(list1)
    row_list = []
    row_num = input("Please enter the number of rows to be added:")
    for i in range(row_num):
        id1 = id1+1
        name = raw_input("Enter name:")
        age = raw_input("Enter age:")
        r1 = "{0},{1},{2}".format(id1,name,age)
        r1 = r1+"\n"
        row_list.append(r1)
    print row_list
    f.writelines(row_list)
    f.close()
def modify_row():
    f1 = open("data1.csv","r")
    data = f1.readlines()
    f1.close()
    modify_data = raw_input("Enter the id of the record to be modified::")
    f2 = 0
    for i in data:
        i = i.split(",")
        if not cmp(i[0], modify_data):
            k= ",".join(i)
            modify_field = raw_input("Which field you need to modify(name/age):")
            modify_field = modify_field.lower()
            
            if modify_field.lower() == "name":
                new_name = raw_input("Enter new name::")
                i[1] = new_name 
                
            elif modify_field.lower() == "age":
                new_age = raw_input("Enter age")
                i[2] = new_age +"\n"
                
            i =",".join(i)
            f2 =1
            break
    if f2:
        print "Data modified"
        data.remove(k)
        data.append(i)
        print data
        f1 = open("data1.csv","w")
        f1.writelines(data)
        f1.close()
    else:
        print "id does not exist"
def delete_row():
    f1 = open("data1.csv","r")
    data1 = f1.readlines()
    f1.close()
    del_id1 = raw_input("Enter the id of row to be deleted::")
    flag = 0
    for i in data1:
        i = i.split(",")
        if not cmp(i[0],del_id1):
            x = ",".join(i)
            print "x=",x
            flag = 1
            break
    if flag:
        print "Data deleted"
        data1.remove(x)
        f1 = open("data1.csv","w")
        f1.writelines(data1)
        f1.close()
if __name__=="__main__":
     while True:
        print "Menu\n 1.Add row\n 2.Modify row\n 3.delete row\n 4.Exit"
        x= raw_input("enter the option::")
        if x=="1":
            add_row()
        elif x=="2":
            modify_row()
        elif x=="3":
            delete_row()
        elif x=="4":
            print "exiting"
            break
