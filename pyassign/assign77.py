"""
77.Remove duplicates elements of the list withoud using built in keywords and temporary list.
"""
l=[1,2,3,4,3,5,6,3,7,4,5]
print "actual list:",l
def remove_duplicates(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst
print "list after removing duplicates:",remove_duplicates(l)
