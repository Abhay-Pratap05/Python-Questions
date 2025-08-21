a = int(input("enter 1st angle:"))
b = int(input("enter 2nd angle:"))
c = int(input("enter 3rd angle:"))

sum = a+b+c

if (sum == 180):
    print("this triangle is valid")
else:
    print("this triangle is not valid")