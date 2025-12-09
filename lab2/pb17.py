n = int(input("Enter a number: "))
n = abs(n)

s = 0
while n > 0:
    digit = n % 10
    s += digit
    n //= 10

print("Sum of digits =", s)
