a = list(map(int,input().split()))
b = int(input("enter no:"))
c = []
for i in a:
    c = c + [i+b]
print(c)