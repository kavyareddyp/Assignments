"""
80.WAP to remove perticular element from a given list for all occurancers
"""
s=[1,2,3,4,3,2]
print "main list:",s
m=[1,2]
print "sublist:",m
for i in s:
    for i in s:
        if i in m:
            del s[s.index(i)]
print  "after removing elements in sublist:",s
        
