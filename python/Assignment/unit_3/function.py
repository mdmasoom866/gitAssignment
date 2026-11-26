# SECTION A -- BASIC FUNCTION PRACTICE :-
# ques -1  display a welcome message 
def display_welcome():
    print("=================================")
    print('''
    welcome to python programming
         let's learn Functions!''')
    print("=================================")
display_welcome();
display_welcome();
display_welcome()


# ques-2 student introduction card
def display_student(name, age, course):
    print("+--------------------------------+")
    print(f"|        STUDENT CARD            |")
    print("+--------------------------------+")
    print(f"| NAME : {name}                   |")
    print(f"| Age : {age}                       |")
    print(f"| Course : {course}                |")
    print("+--------------------------------+")
display_student("Rahul", 18, "B.Tech")


# ques- 3 square, cube , and Double 
def claculate_square():
    num = 4
    print(f"sruare : {num**2}")
def calculate_cube():
    num = 4
    print(f"cube : {num**3}")
def calculate_double():
    num = 4
    print(f"double : {num*2}")
calculate_double();
claculate_square();
calculate_cube()


# ques-4 simple intrest calculator :-
def calculate_simple_intrest(principal, rate, time):
    simple_intrest = (principal*rate*time)//100
    amount = principal + simple_intrest
    print("principal :", principal)
    print("rate: ",rate)
    print("Time: ",time,"year")
    print("simple_intrest: ",simple_intrest)
    print("total_Amount: ",amount)
calculate_simple_intrest(5000,5,2)

# ques 5 Even or Odd Checker
def check_even_odd(number):
    if number%2==0:
        print(number,"is a even number")
    else:
        print(number,"is odd number")
check_even_odd(12);
check_even_odd(7)

# Section B — Parameters, Arguments, and Return Values

# Q6. Find the Larger Number
def find_largest(number_1,number_2):
    if number_1>number_2:
        print(number_1,"is largest number")
    else:
        print(number_2,"is largest number")
find_largest(25,40)


# ques 7. Temperature Converter

def celcius_to_fahrenheit(celsius):
    # fahrenheit = (9/5)*celsius+32
# result = celcius_to_fahrenheit(0)
    return (9/5)*celsius+32
    # print(fahrenheit)
fahrenheit=celcius_to_fahrenheit(0) 
print(fahrenheit)

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
celsius = fahrenheit_to_celsius(98.6)
print(celsius)

# Q8. Understand the Difference Between print() and return

def calculate_sum_1(a, b):
    print(a + b)
result = calculate_sum_1(10, 20)
print(result)
def calculate_sum_2(a, b):
    return a + b
result = calculate_sum_2(10,20)
print(result)

# Q9. Total Marks and Percentage

def calculate_result(marks_1,marks_2,marks_3,marks_4,marks_5):
    total_marks = marks_1+marks_2+marks_3+marks_4+marks_5
    percentage = (total_marks/500)*100
    print("Total Marks :",total_marks)
    print("Percentage :",percentage,"%")
calculate_result(75,80,65,90,70)


# Q10. Rectangle Area and Perimeter

def rectangle_details(length,breadth):
    area = length*breadth
    Perimeter = 2*(length+breadth)
    print("Area: ",area)
    print("perimeter: ",Perimeter)
rectangle_details(10,5)


# Section C — Default and Keyword Arguments

# Q11. Personalized Greeting
# def greet_user(name, message="welcome to python !"):


    

 

