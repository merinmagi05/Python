print("RECTANGLE")
l=int(input("length:"))
b=int(input("breadth:"))
c=lambda x,y: x*y
print("Area of rectangle:"+str(c(l,b)))
print("SQUARE")
s=int(input("side of square:"))
c=lambda x: x*x
print("Area of Square:"+str(c(s)))
print("TRIANGLE")
l=int(input("base:"))
b=int(input("height:"))
c=lambda x,y: .5*x*y
print("Area of Triangle:"+str(c(l,b)))