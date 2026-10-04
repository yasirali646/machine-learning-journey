## Following topics are covered in the file.

#### 1. Waltus Operator ( := ) 
also know as assignment expression operator
It alows you to assign a value to a variable within an expression.

#### 2. Check String or Membership Operator
To check if a certain phrase or character is present or not in a **String**, we can use keyword **in** or **not in**. It is also know as **Membership Operator** if you are working with the **list/tuple/set/dict**.

#### 3. Slicing
By using slicing you can get a part of string from start index to end index. Start index is inclusive and end index is exclusive. You can also give negative index value, if you want to access value from the end.

#### 4. Identity Operator
It is used to compare the object either they are in the same memory location. It can be compared by **is** and **is not** keywords. Equal == operator check the similar value while **is** operator check the same memory location.

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y) # True
print(x is y) # False
print(x is z) # True
print(x is not y) # True
```