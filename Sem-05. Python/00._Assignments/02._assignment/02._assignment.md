# Assignment-2 — Final Answers Only

## Question 1 — String to Integer

### Answer 1
```python
age = "25"
age = int(age)

print(age)
print(type(age))
```

## Question 2 — String to Float

### Answer 2
```python
marks = "75.5"
marks = float(marks)

print(marks)
print(type(marks))
```

## Question 3 — Integer to Float

### Answer 3
```python
number = 50
number = float(number)

print(number)
print(type(number))
```

## Question 4 — Float to Integer

### Answer 4
```python
marks = 85.9
marks = int(marks)

print(marks)
print(type(marks))
```

## Question 5 — Integer to String

### Answer 5
```python
roll_number = 101
roll_number = str(roll_number)

print(roll_number)
print(type(roll_number))
```

## Question 6 — Multiple Conversions

### Answer 6
```python
value1 = "18"
value2 = "92.5"
value3 = 100
value4 = 45.8

value1 = int(value1)
value2 = float(value2)
value3 = str(value3)
value4 = int(value4)

print(value1, type(value1))
print(value2, type(value2))
print(value3, type(value3))
print(value4, type(value4))
```

## Question 7 — Predict the Output

### Answer 7
```text
20
10
25
<class 'int'>
<class 'int'>
<class 'str'>
```

## Question 8 — Debug Type Casting

### Answer 8
```python
age = "19"
new_age = int(age) + 1

print("Age:", new_age)
```

## Question 9 — Marks Conversion

### Answer 9
```python
marks = "85"
marks = int(marks)

final_marks = marks + 5

print("Final Marks:", final_marks)
```

## Question 10 — Price Conversion

### Answer 10
```python
price = "1499.50"
price = float(price)

delivery_charges = 99.50
total_amount = price + delivery_charges

print("Total Amount:", total_amount)
```

---

# Topic 2: Arithmetic Operators

## Question 11 — Basic Arithmetic

### Answer 11
```python
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)
```

## Question 12 — Predict the Output

### Answer 12
```text
3.4
3
2
```

## Question 13 — Operator Precedence

### Answer 13
```text
20
```

```python
result = (10 + 5) * 2
print(result)
```

## Question 14 — More Precedence Practice

### Answer 14
```text
10
```

```python
result = 20 - (4 * 3) + 2
print(result)
```

## Question 15 — Power Operator

### Answer 15
```text
8
9
100
```

```python
side = 5
area = side ** 2

print("Area of Square:", area)
```

## Question 16 — Shopping Bill

### Answer 16
```python
notebook = 80
pen = 20
pencil = 10

total_amount = notebook + pen + pencil

print("Total Amount:", total_amount)
```

## Question 17 — Multiple Quantities

### Answer 17
```python
notebook_price = 50
notebook_quantity = 3
pen_price = 15
pen_quantity = 2
calculator_price = 500
calculator_quantity = 1

notebook_cost = notebook_price * notebook_quantity
pen_cost = pen_price * pen_quantity
calculator_cost = calculator_price * calculator_quantity

total_bill = notebook_cost + pen_cost + calculator_cost

print("Notebook Cost:", notebook_cost)
print("Pen Cost:", pen_cost)
print("Calculator Cost:", calculator_cost)
print("Total Bill:", total_bill)
```

## Question 18 — Complete Groups and Remainder

### Answer 18
```python
students = 47
group_size = 5

complete_groups = students // group_size
students_left = students % group_size

print("Complete Groups:", complete_groups)
print("Students Left:", students_left)
```

## Question 19 — Average Marks

### Answer 19
```python
python_marks = 85
mathematics_marks = 78
physics_marks = 92

total_marks = python_marks + mathematics_marks + physics_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
```

## Question 20 — Percentage

### Answer 20
```python
english = 78
mathematics = 85
python_marks = 92
physics = 81
chemistry = 74

total_marks = english + mathematics + python_marks + physics + chemistry
percentage = total_marks / 500 * 100

print("Total Marks:", total_marks)
print("Percentage:", percentage)
```

---

# Topic 3: Digit Extraction using `%` and `//`

## Question 21 — Ones Digit

### Answer 21
```python
number = 583
ones_digit = number % 10

print("Ones Digit:", ones_digit)
```

## Question 22 — Tens Digit

### Answer 22
```python
number = 583
tens_digit = (number // 10) % 10

print("Tens Digit:", tens_digit)
```

## Question 23 — Hundreds Digit

### Answer 23
```python
number = 583
hundreds_digit = number // 100

print("Hundreds Digit:", hundreds_digit)
```

## Question 24 — Three-Digit Number Analyzer

### Answer 24
```python
number = 746

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
```

## Question 25 — Four-Digit Number

### Answer 25
```python
number = 5829

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
print("Thousands Digit:", thousands_digit)
```

## Question 26 — Sum of Digits

### Answer 26
```python
number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

sum_of_digits = ones_digit + tens_digit + hundreds_digit

print("Sum of Digits:", sum_of_digits)
```

## Question 27 — Four-Digit Sum

### Answer 27
```python
number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

sum_of_digits = ones_digit + tens_digit + hundreds_digit + thousands_digit

print("Sum of Digits:", sum_of_digits)
```

## Question 28 — Product of Digits

### Answer 28
```python
number = 234

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

product_of_digits = ones_digit * tens_digit * hundreds_digit

print("Product of Digits:", product_of_digits)
```

## Question 29 — Reverse a Three-Digit Number

### Answer 29
```python
number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

reversed_number = ones_digit * 100 + tens_digit * 10 + hundreds_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)
```

## Question 30 — Reverse a Four-Digit Number

### Answer 30
```python
number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)
```

## Question 31 — Place Value

### Answer 31
```python
number = 5834

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Thousands Place:", thousands_digit * 1000)
print("Hundreds Place:", hundreds_digit * 100)
print("Tens Place:", tens_digit * 10)
print("Ones Place:", ones_digit)
```

## Question 32 — Difference Between First and Last Digit

### Answer 32
```python
number = 583

hundreds_digit = number // 100
ones_digit = number % 10

difference = hundreds_digit - ones_digit

print("Difference:", difference)
```

## Question 33 — Digit Extraction Debugging

### Answer 33
```python
number = 583
ones = number % 10

print("Ones Digit:", ones)
```

## Question 34 — Four-Digit Extraction

### Answer 34
```python
number = 9365

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
```

## Question 35 — Build a Number

### Answer 35
```python
hundreds = 5
tens = 8
ones = 3

number = hundreds * 100 + tens * 10 + ones

print("Number:", number)
```

---

# Topic 4: Real-Life Arithmetic Problems

## Question 36 — Simple Interest

### Answer 36
```python
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
```

## Question 37 — Rectangle

### Answer 37
```python
length = 15
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
```

## Question 38 — Circle

### Answer 38
```python
radius = 7
pi = 3.14

area = pi * radius ** 2

print("Area:", area)
```

## Question 39 — Temperature Conversion

### Answer 39
```python
celsius = 35

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)
```

## Question 40 — Time Conversion

### Answer 40
```python
total_seconds = 367

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)
```

## Question 41 — Hours, Minutes and Seconds

### Answer 41
```python
total_seconds = 7384

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
```

## Question 42 — Salary Calculation

### Answer 42
```python
basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
```

## Question 43 — Travel Cost

### Answer 43
```python
distance = 120
mileage = 20
fuel_price = 100

fuel_required = distance / mileage
total_fuel_cost = fuel_required * fuel_price

print("Fuel Required:", fuel_required)
print("Total Fuel Cost:", total_fuel_cost)
```

## Question 44 — Shopping Discount

### Answer 44
```python
price = "2500"
discount = "10"

price = float(price)
discount = float(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
```

---

# Topic 5: Type Casting + Arithmetic Operators

## Question 45 — String Numbers

### Answer 45
```python
price = "1200"
quantity = "4"

price = int(price)
quantity = int(quantity)

total_price = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)
```

## Question 46 — Student Result

### Answer 46
```python
python_marks = "85"
math_marks = "78"
physics_marks = "91"

python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)

total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
```

## Question 47 — Bill with Tax

### Answer 47
```python
price = "1500"
quantity = "2"
tax_rate = "5"

price = int(price)
quantity = int(quantity)
tax_rate = int(tax_rate)

subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)
```

## Question 48 — Discount + GST

### Answer 48
```python
price = 2000
discount_rate = 15
gst_rate = 18

discount_amount = price * discount_rate / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst_rate / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)
```

## Question 49 — Debug the Billing Program

### Answer 49
```python
price = "500"
quantity = 3

price = int(price)

total = price * quantity

print("Total:", total)
```

## Question 50 — Debug the Marks Program

### Answer 50
```python
marks1 = "80"
marks2 = "75"
marks3 = "90"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3

print("Total Marks:", total)
```

---

# Topic 6: Output Prediction and Conceptual Practice

## Question 51 — Type Casting Output

### Answer 51
```text
50
50
<class 'str'>
<class 'int'>
```

## Question 52 — Float to Integer

### Answer 52
```text
99.99
99
```

## Question 53 — Arithmetic Output

### Answer 53
```text
17
7
60
2.4
2
2
```

## Question 54 — Parentheses Challenge

### Answer 54
```text
20
30
7.0
2.5
```

## Question 55 — Digit Challenge

### Answer 55
```text
4
8
6
```

- `a` = Ones
- `c` = Tens
- `d` = Hundreds

---

# Topic 7: Mixed Debugging

## Question 56 — Debug the Student Program

### Answer 56
```python
student_name = "Ravi"
marks = "85"

marks = int(marks)
total = marks + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))
```

## Question 57 — Debug the Number Program

### Answer 57
```python
number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)
```

## Question 58 — Debug the Discount Program

### Answer 58
```python
price = "2000"
discount = "15"

price = int(price)
discount = int(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)
```

## Question 59 — Complete Debugging Challenge

### Answer 59
```python
student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))
```

## Question 60 — Final Challenge: Number + Billing

### Answer 60
```python
number = 5836

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + ones_digit

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

price = "1250"
quantity = "4"
discount = "10"

price = int(price)
quantity = int(quantity)
discount = int(discount)

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
```

### Output
```text
Thousands Digit: 5
Hundreds Digit: 8
Tens Digit: 3
Ones Digit: 6
Sum of Digits: 22
Reversed Number: 6385
Subtotal: 5000
Discount Amount: 500.0
Final Amount: 4500.0
```
