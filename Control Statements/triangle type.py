a = int(input("enter 1st angle:"))
b = int(input("enter 2nd angle:"))
c = int(input("enter 3rd angle:"))

sum = a+b+c

if (sum ==180):
    if (a==90 or b==90 or c==90):
        print("this is a right angle triangle")
    elif (a>90 or b>90 or c>90 ):
        print("this is a obtuse angle triangle")
    else:
        print("this is an acute angle triangle")
else:
    print("this triangle is not valid")