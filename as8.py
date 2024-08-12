#Using Smallest and Largest iterable
smallest = 0
largest = 0
#Putting the loop to 5 numbers 
for a in range (5):
    #The user entering his input
    x= (input("enter the number"))
    #putting value of x 
    if a == 0:
        smallest = largest = x
    else:
        if (smallest> x):
            smallest = x
        else:
             if (x> largest):
                 largest= x
                 #Print the Values
        print("This Number is Largest", largest)
    print("This Number is smallest", smallest)

