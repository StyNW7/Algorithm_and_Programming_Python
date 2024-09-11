# Arithmetic Operators

print("Arithmetic Operators:\n\n")

num1 = 10
num2 = 3

print (num1+num2) # Addition
print (num1-num2) # Substraction
print (num1*num2) # Multiplication
print (num1/num2) # Division
print (num1%num2) # Modulo
print (num1**num2) # Power
print (num1//num2) # Floor Division

# Precedences and Associative Operators

print("Associative Operators:\n\n")

total1 = (num1 + num2) * num2
print (total1)

total2 = num1 + num2 * num2
print (total2)

result = 10 + 5 * 2  # Output: 20
print(result)

result = (10 + 5) * 2  # Output: 30
print(result)

# Assignment Operators

print("Assignment Operators:\n\n")

x = 10
x += 5  # Is the same as x = x + 5
print(x)  # Output: 15
x *= 2  # Is the same as x = x * 2
print(x)  # Output: 30

# Relational Operators

print("Relational Operators:\n\n")

a = 10
b = 5

print(a > b)  # Output: True
print(a == b)  # Output: False
print(a != b)  # Output: True

# Logical Operators

print("Logical Operators:\n\n")

x = 7
print(x > 5 and x < 10)  # Output: True
print(x < 5 or x > 10)   # Output: False
print(not(x > 5))        # Output: False

# Bitwise Operators

print("Bitwise Operators:\n\n")

a = 5  # 5 in binary is 101
b = 3  # 3 in binary is 011

print(a & b)  # Output: 1 (001 in binary)
print(a | b)  # Output: 7 (111 in binary)
print(a ^ b)  # Output: 6 (110 in binary)
print(~a)     # Output: -6 (complement of 5)
print(a << 1) # Output: 10 (shift to left, 1010 in binary)
print(a >> 1) # Output: 2 (shift to right, 10 in binary)