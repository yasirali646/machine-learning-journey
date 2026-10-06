
x = 10
y = 5.5

print("*" * 50)
print("Arthemetic Operator")
print("*" * 50)

# Arthemetic Operator
print("Addition: ", x + y)
print("Subraction: ", x - y)
print("Multiplication: ", x * y)
print("Division: ", x / y)
print("Floor division: ", x // y)
print("Exponentiation: ", x ** y)
print("Modulus: ", x % y)


print("\n")
print("*" * 50)
print("Assignment Operator")
print("*" * 50)

# Assignment Operator
z = 100
z += 10
print("Z after += :", z)

z -= 5
print("Z after -= :", z)

z *= 7
print("Z after *= :", z)

z /= 2
print("Z after /= :", z)

z %= 10
print("Z after %= :", z)

z //= 2
print("Z after //= :", z)

z **= 10
print("Z after **= :", z)

z = 5
# Bitwise AND operator
z &= 3
print("Z after &= :", z)

"""
Explanation:

The & symbol is the bitwise AND operator. It compares each bit of the two numbers in binary:
A bit becomes 1 only if both corresponding bits are 1.
Otherwise, the bit becomes 0.

Decimal 5 in binary = 101
Decimal 3 in binary = 011

  1 0 1 (5)
& 0 1 1 (3)
-------
  0 0 1   (1 in decimal)


Note: bitwise operators only work with integer values.

"""

# Bitwise OR operator
z |= 3
print("Z after |= :", z)
"""
  0 0 1 (1)
| 0 1 1 (3)
-------
  0 1 1   (3 in decimal)
"""

z = 5
# Bitwise XOR operator
z ^= 3
print("Z after ^= :", z)
"""
Explanation:

Leftmost bit:  1 XOR 0 -> 1 (different)
Middle bit:    0 XOR 1 -> 1 (different)
Rightmost bit: 1 XOR 1 -> 0 (same)

  1 0 1   (5)
^ 0 1 1   (3)
-------
  1 1 0   (6 in decimal)
"""

# Bitwise right shift operator

# Example 1:
z = 40
z >>= 3
print("Z after >>= :", z)

z = 40
print("Z after // :", z // 8)
# or
print("Z after z // (2 ** 3) :", z // (2 ** 3))


#Example 2:
z = 40
z >>= 5
print("Z after >>= :", z)

z = 40
print("Z after // :", z // 32)
# or
print("Z after z // (2 ** 5) :", z // (2 ** 5))


"""
Explanation:

x = x >> 3 (or x >>= 3) moves all the binary bits of x to the right by 3 positions. 
The 3 rightmost bits are discarded.

Binary View:
Decimal 40 in binary: 101000

Shift right by 3 (drop the last 3 bits):

1 0 1 [0 0 0]  -->  1 0 1   (5 in decimal)


The Mathematical Shortcut
Shifting bits right by n positions is identical to integer floor division by 2**n.

x // 8

Example 1:
z >>= 3
2**3 = (2 * 2 * 2) = 8

Example 2:
z >>= 5
2**5 = (2 * 2 * 2 * 2 * 2) = 32



"""

# Bitwise left shift operator

# Example 1:
z = 5
z <<= 4
print("Z after <<= :", z)

z = 5
print("Z after z*16 :", z * 16)
# or
print("Z after z * 2**4 :", z * (2 ** 4))

# Example 2:
z = 48
z <<= 6
print("Z after <<= :", z)

z = 48
print("Z after z*8 :", z * 64)
# or
print("Z after z*(2 ** 6) :", z * (2 ** 6))


"""
Explanation:

x = x << 3 (or x <<= 3) moves all binary bits of x to the left by 3 positions, 
filling the vacated positions on the right with zeros.

Binary View:
Decimal 5 in binary: 101

Shift left by 3 (append three 0s):

1 0 1  -->  1 0 1 [0 0 0]   (40 in decimal)


The Mathematical Shortcut
Shifting bits left by n positions is identical to multiplying by 2**n:

x * 2**3 = x * 8

Example 1:
z <<= 4
2**4 = (2 * 2 * 2 * 2) = 16

Example 2:
z <<= 6
2**6 = (2 * 2 * 2 * 2 * 2 * 6) = 64

"""

# Walnut Operator (assignment expression)
print("W after w:=5 :", w := 5)

print("\n")
print("*" * 50)
print("Ternary Operator")
print("*" * 50)

age = 10
message = "You are an adult" if age >= 18 else "You are a teenger."
print(message)

num = 7
day = "Friday" if num == 5 else "Saturday" if num == 6 else "Sunday" if num == 7 else "Weekday"
print(day)


print("\n")
print("*" * 50)
print("Compare Operators")
print("*" * 50)

x = 5
y = 7

print("Equal (x == y): ", x == y)
print("Not Equal (x != y): ", x != y)
print("Greater Than (x > y): ", x > y)
print("Less Than (x < y): ", x < y)
print("Greater Than or Equal (x >= y): ", x >= y)
print("Less Than or Equal (x <= y): ", x <= y)


print("\n")
print("*" * 50)
print("Logical Operators")
print("*" * 50)


x = 10
y = 55

print("AND Operator  x > 5 and y < 100: ", x > 5 and y < 100)
print("OR Operator x != 44 or y == 55: ", x != 44 or y == 55)
print("NOT Operator not (x != 44 | y == 55): ", not(x != 44 and y == 55))


print("\n")
print("*" * 50)
print("Identity Operators")
print("*" * 50)



x = 18
y = 22
z = y

print("IS Operator: (x is y) ", x is y)
print("IS Operator: (y is z) ", y is z)
print("IS NOT Operator: (x is not z) ", x is not z)


print("\n")
print("*" * 50)
print("Membership Operators")
print("*" * 50)

message = "This is an example of string"

print("IN Operator : ", "example" in message)
print("IN Operator : ", "apple" in message)
print("NOT IN Operator : ", "banana" not in message)

print("\n")
print("*" * 50)
print("Bitwise Operators")
print("*" * 50)


x = 7
y = 4

print("AND Operator: ", x & y)
print("OR Operator: ", x | y)
print("XOR Operator: ", x ^ y)
print("NO/Inverse tOperator: ", ~x)
print("Left Shift Operator: ", x << y)
print("Right Shift Operator: ", x >> y)

