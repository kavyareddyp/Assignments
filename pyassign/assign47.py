## Input=["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']]
list1 = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"]
def myfunc(lst):
    ret = []
    a = b = lst[0]                           

    for el in lst[1:]:
        if el == b+1: b = el                 
        else:                                
            ret.append(a if a==b else (a,b)) 
            a = b = el                       
    ret.append(a if a==b else (a,b))         
    return ret
list2=[]
x=[]
for i in list1:
    if type(i)==str:
        list2.append(list(i))
for i in list2:
    x.append(i[0])
y=list(set(x))
ylist1=[]
ylist2=[]
for i in list2:
    if i[0]==y[0]:
        ylist1.append(int(i[2]))
    else:
        ylist2.append(int(i[2]))

l1=myfunc(ylist1)
l2=myfunc(ylist2)
ol=[]
for i in l1:
    a=["{0}/{1}".format(y[0],i)]
    ol.append(a)
for i in l2:
    a=["{0}/{1}".format(y[1],i)]
    ol.append(a)
print "input:",list1
print "output:", ol
    
    
    



            

