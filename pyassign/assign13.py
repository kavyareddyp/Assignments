"""
13.take a string from the user and check contains atleast one alphabets or not?
"""
s=raw_input("Enter a string:")
for i in s:
    if i.isdigit()==False:
        print "string has characters"
        break
else:
    print "string does not contains alphabets"
