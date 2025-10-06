p=int(input("enter principle amount:"))
r=float(input("enter rate of interest:"))
t=int(input("enter time period:"))
si=(p*r*t)/100
print("simple interest is :",si)

ci= p* ((1 + r/ 100) ** t) -p
print("compund interest is :",ci)



