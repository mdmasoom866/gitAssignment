#ans-1
age = "25"
print(int(age))

#ans-2
marks = "75.5"
print(float(marks))

#ans-3
number = 50
print(float(number))

#ans-4
marks = 85.9
print(int(marks))

#ans-5
roll_number = 101
print(str(roll_number))

#ans-6
print(int("18"))
print(float("92.5"))
print(str(100))
print(int(45.8))

#ans-7
a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

#ans-8
age = "19"
new_age = age + "1"

print("Age:", new_age)

#ans-9
marks = "85"
print(int(marks)+5)

#ans-10
price = "1499.50"
print(float(price)+99.50)

#ans-11
a = 20
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

#ans-12
a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)
#the three results are different because single slash is division sign doble slice is floor division sign and % sign is remainder sign.these all sign are different and their function are totally diffent.

#ans-13
result = 10 + 5 * 2
print(result)
result = (10 + 5) * 2
print(result)

#ans-14
result = 20 - (4 * 3) + 2
print(result)

#ans-15
side = 5
area_of_square=(side**2)
print(area_of_square)

#ans-16
x=80
y=20
z=10
print(x+y+z)

#ans-17
notebook=50*3
pens=15*2
calculator=500*2
total_bill=notebook+pens+calculator
print("price of notebooks=",notebook)
print("price of pens=",pens)
print("price of calculator=",calculator)
print("total bill",total_bill)

#ans-18
total_students=47
no_of_groups=5
complete_groups=total_students//no_of_groups
student_left=total_students%no_of_groups
print(complete_groups)
print(student_left)

#ans-19
python=85
maths=78
physics=92
total_marks=python+maths+physics
total_subject=3
average_marks=total_marks/total_subject
print("average_marks=",average_marks)

#ans-20
eng=78
maths=85
python=92
physics=81
chemistry=74
total_marks=eng+maths+python+physics+chemistry
percentage=(total_marks/500)*100
print("total marks=",total_marks)
print("percentage=",percentage)

#question 21

number = 583
ones = number % 10

print("Ones Digit:", ones)


#question 22


number = 583
tens = (number // 10) % 10

print("Tens Digit:", tens)



#question 23


number = 583
hundreds = number // 100

print("Hundreds Digit:", hundreds)


#question 24

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)



#question 25

number = 5829

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)
print("Thousands Digit:", thousands)



#question 26


number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

digit_sum = hundreds + tens + ones
print("Sum of Digits:", digit_sum)



#question 27


number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

digit_sum = thousands + hundreds + tens + ones
print("Sum of Digits:", digit_sum)


#question 28

number = 234

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

product = hundreds * tens * ones
print("Product of Digits:", product)



#question 29

number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

reversed_number = (ones * 100) + (tens * 10) + hundreds

print("Original Number:", number)
print("Reversed Number:", reversed_number)


#question 30

number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Original Number:", number)
print("Reversed Number:", reversed_number)



#question 31

number = 5834

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Thousands Place:", thousands * 1000)
print("Hundreds Place:", hundreds * 100)
print("Tens Place:", tens * 10)
print("Ones Place:", ones)


#question 32
number = 583

ones = number % 10
hundreds = number // 100

difference = hundreds - ones
print("Difference:", difference)


#question 33


number = 583
ones = number % 10
print("Ones Digit:", ones)


#question 34

number = 9365

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)



#question 35

hundreds = 5
tens = 8
ones = 3

number = (hundreds * 100) + (tens * 10) + ones
print("Number:", number)


#question 36

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


#question 37

length = 15
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area:", area, "sq cm")
print("Perimeter:", perimeter, "cm")


#question 38

radius = 7
pi = 3.14

area = pi * (radius ** 2)

print("Area of Circle:", area, "sq cm")


#question 39


celsius = 35
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


#question 40


total_seconds = 367

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)



#question 41

total_seconds = 7384

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


#question 42


basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)



#question 43

distance = 120
mileage = 20
fuel_price = 100

fuel_required = distance / mileage
total_fuel_cost = fuel_required * fuel_price

print("Fuel Required:", fuel_required, "litres")
print("Total Fuel Cost: ₹", total_fuel_cost)


#question 44

price = "2500"
discount = "10"

price_num = float(price)
discount_num = float(discount)

discount_amount = price_num * (discount_num / 100)
final_price = price_num - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)


# Question 45 — String Numbers
price = "1200"
quantity = "4"
p_int = int(price)
q_int = int(quantity)
print("Price:", p_int)
print("Quantity:", q_int)
print("Total Price:", p_int * q_int)



# Question 46 — Student Result


python_marks = "85"
math_marks = "78"
physics_marks = "91"
tot = int(python_marks) + int(math_marks) + int(physics_marks)
print("Total Marks:", tot)
print("Average Marks:", tot / 3)



# Question 47 — Bill with Tax



price = "1500"
quantity = "2"
tax_rate = "5"
subtotal = float(price) * int(quantity)
tax_amount = subtotal * (float(tax_rate) / 100)
print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", subtotal + tax_amount)



# Question 48 — Discount + GST


cost = 2000
disc_amount = cost * 0.15
price_after_disc = cost - disc_amount
gst_amount = price_after_disc * 0.18
final_price = price_after_disc + gst_amount
print("Discount Amount:", disc_amount)
print("Price after Discount:", price_after_disc)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)



# Question 49 — Debug the Billing Program


price = "500"
quantity = 3
total = int(price) * quantity
print("Total:", total)





# Question 50 — Debug the Marks Program
marks1 = "80"
marks2 = "75"
marks3 = "90"
total = int(marks1) + int(marks2) + int(marks3)
print("Total Marks:", total)


# Question 51 — Type Casting Output

a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))

# Output:
# 50
# 50
# <class 'str'>
# <class 'int'>


# Question 52 — Float to Integer

number = 99.99
result = int(number)

print(number)
print(result)

# Output:
# 99.99
# 99
# Explanation: Casting a float to int truncates (discards) the decimal portion without rounding.


# Question 53 — Arithmetic Output

a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Output:
# 17
# 7
# 60
# 2.4
# 2
# 2


# Question 54 — Parentheses Challenge

print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))

# Output:
# 20
# 30
# 7.0
# 2.5
# Explanation: Parentheses override standard operator precedence, evaluating operations inside them first.


# Question 55 — Digit Challenge

number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)

# Output:
# 4
# 8
# 6
# Variable Identification:
# a = Ones digit (4)
# c = Tens digit (8)
# d = Hundreds digit (6)


# Question 56 — Debug the Student Program

student_name = "Ravi"
marks = "85"

total = int(marks) + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))


# Question 57 — Debug the Number Program

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)


# Question 58 — Debug the Discount Program

price = "2000"
discount = "15"

price_num = float(price)
discount_num = float(discount)

discount_amount = (price_num * discount_num) / 100
final_price = price_num - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)


# Question 59 — Complete Debugging Challenge

student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

total = int(marks1) + int(marks2) + int(marks3)
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))


# Question 60 — Final Challenge: Number + Billing

# Part A — Number Analysis
number = 5836

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

sum_of_digits = thousands + hundreds + tens + ones
reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)



# Part B — Product Billing



price = "1250"
quantity = "4"
discount = "10"

price_num = float(price)
quantity_num = int(quantity)
discount_num = float(discount)

subtotal = price_num * quantity_num
discount_amount = subtotal * (discount_num / 100)
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
