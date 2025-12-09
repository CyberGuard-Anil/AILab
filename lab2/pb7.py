a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is", a)
elif b <= a and b <= c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)

