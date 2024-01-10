a=str(input("Enter a string:"))
fchar=a[0]
a=a.replace(fchar,"$")
a=fchar+a[1:]
print(a)