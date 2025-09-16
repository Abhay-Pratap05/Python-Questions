a = list(map(int,input().split()))
max = a[0]
min = a[0]
for i in range(len(a)):
    if (max<a[i]):
        max = a[i]
    if (min>a[i]):
        min = a[i]

print("max=",max)
print("min=",min)
    