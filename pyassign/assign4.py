"""
4.take a number from the user and check whether it is prime?
"""
num=input("Enter a number:")
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print num,"is not a prime number"
            print i,"is a factor of ",num
            break
    else:
        print num,"is a prime number"
else:
   	print num,"is not a prime number"
