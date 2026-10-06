x = 10
y = 78

# Simple if condition
if y > x:
    print("Y is greater than X")


# Multiple if condition
if y >= x:
    print("Y is greater than or equal to X")
if y < x:
    print("Y is less than X")
if y <= x:
    print("Y is less than or equal to X")
if y == x:
    print("Y is equal to X")
if y != x:
    print("Y is not equal to X")


# if else condition
day = 6

if day > 5:
    print("Hurray! Today is Weekend")
else:
    print("Today is Weekday")


# if elif condition
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  """
When you use elif, Python evaluates the conditions from top to bottom. 
As soon as it finds a condition that is true, it executes that block and skips all remaining conditions  
  """

# if elif else condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short hand if
a = 5
b = 2

# Example 1
if a > b: print("a is greater than b")

# Example 2
print("A") if a > b else print("B")

# Example 3
bigger = a if a > b else b
print("Bigger is ", bigger)

# Example 4
print("A") if a > b else print("=") if a == b else print("B")


# if with Logical operators
a = 200
b = 33
c = 500

# AND Operator
if a > b and c > a:
  print("Both conditions are True")


# OR Operator
if a > b or a > c:
  print("At least one of the conditions is True")


# NOT Operator
if not a > b:
  print("a is NOT greater than b")


# Combining Multiple Operators

# Example 1
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# Example 2
username = "Yasir"
password = "123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

# Example 3
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")


# Nested If condition

# Example 1
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# Example 2
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


# Example 3
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")