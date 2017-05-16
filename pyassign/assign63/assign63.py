"""
63.Take three columns disease, symptoms, advice in a file and fill the details
Ask the user to enter symptoms. Based on this symptoms Suggest the user to what disease it may be and few advices.
"""
import csv
symptoms=raw_input("enter a symtoms")
with open(r'D:\Assignmentstosubmit\assign63\diseasefile.csv','r') as df:
    ufr=csv.reader(df)
    list1=[]
    for row in ufr:
        list1.append(row)
    for i in list1:
        if symptoms in i:
            print "disease:{0} and advice:{1}" .format(i[0],i[2])
            break
        else:
            print "File doesnot information about entered symptoms"
            break


