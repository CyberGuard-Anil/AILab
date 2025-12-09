n = int(input("Enter a number: "))
x = abs(n)

if 0 <= x <= 9:
    print("Single digit number")
elif 10 <= x <= 99:
    print("Two digit number")
elif 100 <= x <= 999:
    print("Three digit number")
else:
    print("More than three digits")
