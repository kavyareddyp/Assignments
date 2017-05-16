"""
2.write a program to chek given substring is there in actual string or not? 
"""
s=raw_input("Enter main string:")
k=raw_input("Enter sub string to find:")
if k.lower() in s.lower():
    print "string found"
else:
    print "string not found"
