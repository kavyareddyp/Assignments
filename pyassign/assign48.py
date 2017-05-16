"""
48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
"""
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
def myfunc(lst):
    ret = []
    a = b = lst[0]
    for el in lst[1:]:
        if el == b+1:
                b = el                 
        else:                                
            ret.append(a if a==b else (a,b)) 
            a = b = el                       
    ret.append(a if a==b else (a,b))         
    return ret
x=myfunc(l)
print "Input:",l
print "output:",x
