"""
39. find the start position of the largest block of repeated characters in a given string
"""
#It works if we enter the words rather a combine string
s=raw_input("enter a words:")
j=s.split(' ')
k=raw_input("enter a characters:")
l=0
for i in j:
    c=i.count(k)
    h=len(i)
    if c >l:
        l=c
for i in j:
    if l==i.count(k): 
        print "The start position of larget block of repeated characters in a given string:",j.index(i)

# it works with a combined string
str1=raw_input("Enter the string to find out the largest block index")
str2=""
str3=[]
index1 = 0
for i in range(len(str1)):
    if i==((len(str1))-1):
        str2 = str2+str1[i]
        str3.append(str2)
        str2=""
    else:
        if str1[i]==str1[i+1]:
            str2 =str2+str1[i]
            
        else:
            str2 = str2+str1[i]
            str3.append(str2)
            str2=""
index1 = 0
str4 = ""
str5 = []
str6 = []

for i in range(len(str3)):

    if index1 < len(str3[i]):
               index1 = len(str3[i])
               str4 = str3[i]

for i in range(len(str3)):
    if index1 == len(str3[i]):
        str6.append(str3[i])
        str5.append(str1.index(str3[i]))

print "Index of the largest block {0} in the given string is {1} respectively".format(str6,str5)
        

