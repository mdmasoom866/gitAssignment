# Ques - 1
for i in range(2, 15, 3):
    print(i)
# it will print 2 5 8 11 14 because for tgis loop the starting value is 2 and ending value is 15 with the step value 3 .
 
#  Ques -2 
for i in range(15, 2, -3):
    print(i)
    # it will print 15  13 11 8 5 

# Ques - 3
for i in range(4, 31, 5):
    print(i)          
    # it will print 4 9 14 19 24 28 

# Ques - 4
for i in range(3, 19, 3):
    print(i)
    # it wil print 3 6 9 12 15 18

# Ques - 5 
#  Print each number from 5 to 10 along with its distance from 20.
for i in range(5,11):
    print(i,20-i)

# Ques - 6
# For every number from 1 to 6, print the number, its square, and its cube on one line.

for i in range(1,7):
    print(i,i*2,i**3)

# Quse - 7 
# Take start and end. Find the sum of all integers from start to end using one for loop.
sum=0
for i in range(5,11):
    sum=sum+i
print("sum of all numbers = ",sum)    


# Ques - 8 
# Take N and count how many numbers from 1 to N are divisible by 3.

num = 10
count=0
for i in range(1,num+1):
    if i%3==0:
        count=count+1
print("Count =",count)   

# Ques - 9 
# Take N and calculate the sum of all numbers from 1 to N divisible by 4.

num = 20 ;
sum=0
for i in range(1,num+1):
    if i%4==0:
        sum=sum+i
print("sum =",sum)


# Ques - 10
# num = int (input("Enter an number N :"))
# count = 0
# for i in range(1,num+1):
#     if i%3==0 and i%5==0:
#         count=count+1
# print("count = ", count)        



# Ques - 11 
# num = int(input("Enter an number N :"))
# sum=0
# for i in range(1,num+1):
#     if i%3!=0:
#         sum=sum+i
# print("sum = ",sum)

# Ques - 12 
# num = int(input("Enter a number N : "))
# even=0
# odd=0
# for i in range(1,num+1):
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print(f"Even ={even} , odd={odd}")

# Ques - 13 
# num = int(input("Enetr a number N :"))
# sum = 0
# for i in range(1,num+1):
#     sum=sum+i
#     print(sum)
# print()    

# Ques - 14 
# num = int(input("Enter a number N :"))
# multiply = 1
# for i in range(1,num+1):
#     multiply=multiply*i
#     print(multiply)
# print()    


# Ques - 15 
# num = int(input("Eneter a number N  :"))
# factorial = 1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(factorial)    


# Ques - 16 
# num = int(input( "Enter a number N :"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
#     print(f"{i}! = {factorial}")
# print()    

# Ques - 17 
# num = int( input("ENter e numbee N :"))
# even =1
# odd =1
# for i in range(1,num+1):
#     if i%2==0:
#         even=even*i
# print(even)        
   
# Ques - 18
# num = int(input("Enter a number N :"))
# odd =1
# for i in range(1,num+1):
#     if i%2!=0:
#         odd=odd*i
# print("Output = ",odd)        


# Ques - 19 
# num = int(input("Enter a even number N :"))
# product = 1
# for i in range(num,0,-2):
#     product=product*i
# print("Output = ",product)    

# Ques - 20
# Take N and calculate:
# 1² + 2² + 3² + ... + N²

# num = int(input("enter a number N :"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i**2
# print("Output = ",sum)    

# Ques - 21
# Take N and calculate:
# 1³ + 2³ + 3³ + ... + N³

# num = int(input("Enter a number N :"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+1**3
# print("Output = ",sum)    

# Ques - 22
#Take N and calculate:
# 1! + 2! + 3! + ... + N!

# num=int(input("Enter a number N :"))
# sum=0
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
#     sum=sum+factorial
# print(sum)    


# Ques - 23
# Take a positive integer and count its digits using a for loop. Do not convert the number to a string.

num = "12345"
count=0
for i in num:
    count=count+1
print(count)    


# Ques - 24
# Take an integer and find the sum of its digits using one for loop.

# num = int(input("Enter a number :"))
# count=0
# for i in range(1,num+1) :
#     count=count+i
# print(count)    


# Ques - 25
# Take an integer and find the product of its digits.

# num = int(input("Enter a number"))
# multy = 1
# for i in range(1,num+1):
#     multy=multy*i
# print(multy)    

# Ques - 26
# Count how many digits of a given integer are even.


# Ques - 27
# Find the sum of only the even digits of a number.
# num = int(input("enter a number :"))
# sum=sum+0
# for num in range(1,num+1):
#     if num%2==0:
#         sum=sum+0
# print(sum)        


#  Ques - 28
# Find the largest digit of a number using one for loop. Do not use max() and do not convert the number to a string.

num=int(input("Enter the a Number: "))
digit=int(math.log10(num))+1
largest=0
for i in range(digit):
    if num%10>largest:
        largest=num%10
    num=num//10
print(largest)

# Q29. Smallest Digit Without min()

num=int(input("Enter the a Number: "))
digit=int(math.log10(num))+1
smallest=10
for i in range(digit):
    if num%10<smallest:
        smallest=num%10
    num=num//10
print(smallest)

# Q30. Reverse a Number

num=int(input("Enter the Number: "))
digit=int(math.log10(num))+1
rev=0
for i in range(digit):
    rev=rev+num%10
    rev=rev*10
    num=num//10
rev=rev//10
print(rev)

# Q31. Palindrome Number

num=int(input("Enter the Number: "))
pallindrome_check=num
digit=int(math.log10(num))+1
rev=0
for i in range(digit):
    rev=rev+num%10
    rev=rev*10
    num=num//10
rev=rev//10
if rev==pallindrome_check:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q32. Count a Specific Digit

num=int(input("Enter a Number: "))
digit=input("Enter the digit to count: ")
check_num=str(num)
count=0

for i in check_num:
    if i==digit:
        count=count+1
print(count)

# Q33. First Digit Using Repeated Division

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1
for i in range(digit):
    n=n//10
    if n>0 and n<10:
        print(n)

# Q34. Difference Between Largest and Smallest Digit

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1
max=0
min=10
for i in range(digit):
    if n%10>max:
        max=n%10
    if n%10<min:
        min=n%10
    n=n//10
print(max)
print(min)
print(max-min)

# Q35. Digit Position Value

n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1

for i in range(1,digit+1):
    print(n%10,i)
    n=n//10

# Q36. Armstrong Number — 3 Digit

n=int(input("Enter a Number: "))
check_no=n
digit=int(math.log10(n))+1
arm_no=0
for i in range(digit):
    arm=arm_no+(n%10)**digit
    n=n//10
if arm_no==check_no:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")




# Q37. Print Characters with Index

string=input("Enter a string: ")
for i in range(0,len(string)):
    print(i,string[i])

# Q38. Count Characters Without len()

string=input("Enter a string: ")
count=0
for i in string:
    count=count+1
print(count)

# Q39. Count Vowels and Consonants

string=input("Enter a string: ")
vowel_count=0
consonent_count=0
for i in string:
    if i.lower() in "aeiou" :
        vowel_count=vowel_count+1
    elif i.lower() not in " aeiou":
        consonent_count=consonent_count+1
print(f"Vowels = {vowel_count}, Consonents = {consonent_count}")

# Q40. Character Frequency

string=input("Enter a string: ")
frequency_count=input("Enter the string for the frequency count: ")
count=0
for i in string:
    if i==frequency_count:
        count=count+1

print(f"{frequency_count} = {count}")

# Q41. First Occurrence Position

string=input("Enter a string: ")
first_occurence=input("Enter the character for the first occurence: ")
found=False
for i in range(0,len(string)):
    if string[i]==first_occurence and not found:
        print(i)
        found=True
if not found:
    print("Not Found")

# Q42. Count Uppercase and Lowercase

s = input("Enter a string: ")
upper = 0
lower = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1

print("Uppercase =", upper, end=", ")
print("Lowercase =", lower)

# 43. Character Code Analyzer

string=input("Enter a string: ")
for i in range(0,len(string)):
    print(string[i],ord(string[i]))

# Q44. String Without Vowels

string=input("Enter a string: ")
no_vowel=""
for i in string:
    if i.lower() not in "aeiou":
        no_vowel=no_vowel+i
print(no_vowel)

# Level 6 — Midpoint, Half & String Logic

# Q45. Find the Middle Character

# s = input()
# mid = len(s) // 2

# for i in range(len(s)):
#     if i == mid:
#         print(s[i])

# Q46. First Half and Second Half

string=input("Enter a string with even no. of character: ")

half=len(string)/2

first_half=""
second_half=""

for i in range(len(string)):
    if i<half:
        first_half=first_half+string[i]
    else:
        second_half=second_half+string[i]
print("First half: ",first_half)
print("Second half: ",second_half)



import math

# Q47. Split a String by Length — Odd vs Even
s = input("Enter a string: ")
n = len(s)
half = n // 2
first_half = ""
second_half = ""
mid = ""

for i in range(n):
    if i < half:
        first_half += s[i]
    elif n % 2 != 0 and i == half:
        mid = s[i]
    else:
        second_half += s[i]

print("First Half:", first_half)
if mid != "":
    print("Middle:", mid)
print("Second Half:", second_half)

# Q48. Compare Two Halves
s = input("Enter a string of even length: ")
n = len(s)
half = n // 2
first_half = ""
second_half = ""

for i in range(n):
    if i < half:
        first_half += s[i]
    else:
        second_half += s[i]

if first_half == second_half:
    print("Equal Halves")
else:
    print("Different Halves")

# Q49. Mirror the String
s = input("Enter a string: ")
n = len(s)
is_symmetric = True

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_symmetric = False

if is_symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")

# Q50. Alternate Character Extraction
s = input("Enter a string: ")
alt_string = ""

for i in range(len(s)):
    if i % 2 == 0:
        alt_string += s[i]
print(alt_string)

# Q51. Count Characters at Even and Odd Indexes
s = input("Enter a string: ")
even_count = 0
odd_count = 0

for i in range(len(s)):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even Index = {even_count}, Odd Index = {odd_count}")

# Q52. Swap Adjacent Characters
s = input("Enter a string with even length: ")
swapped = ""

for i in range(0, len(s), 2):
    swapped += s[i+1] + s[i]
print(swapped)

# Q53. Second Largest Digit
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
largest = -1
second_largest = -1

for i in range(digit_count):
    digit = num % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    num = num // 10
print(second_largest)

# Q54. Longest Consecutive Equal Character Run
s = input("Enter a string: ")
max_run = 0
current_run = 0
prev_char = ""

for char in s:
    if char == prev_char:
        current_run += 1
    else:
        current_run = 1
        prev_char = char
    if current_run > max_run:
        max_run = current_run
print(max_run)

# Q55. Most Frequent Character — Controlled Approach
s = input("Enter a string: ")
target = input("Enter a target character: ")
count = 0
total_chars = 0

for char in s:
    total_chars += 1
    if char == target:
        count += 1

frequency = (count / total_chars) * 100
print(f"Count = {count}, Frequency = {frequency}%")

# Q56. Running Digit Sum Until the End
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
running_sum = 0

for i in range(digit_count):
    running_sum += num % 10
    print(running_sum)
    num = num // 10

# Q57. Number with Most Even Digits
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
even_count = 0
odd_count = 0

for i in range(digit_count):
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10

if even_count > odd_count:
    print("More Even Digits")
elif odd_count > even_count:
    print("More Odd Digits")
else:
    print("Equal")

# Q58. Alternating Digit Sum
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
alt_sum = 0
sign = 1

for i in range(digit_count):
    digit = num % 10
    alt_sum += digit * sign
    sign *= -1  # Flips between 1 and -1
    num = num // 10
print(alt_sum)

# Q59. Output Prediction — Accumulator Trap
"""
Expected Output:
2
6
12
20
30
"""

# Q60. Output Prediction — Condition Inside Loop
"""
Expected Output:
5
Explanation: The loop runs from 1 to 10. The condition i % 2 == 0 checks if the number is even. There are 5 even numbers between 1 and 10 (2, 4, 6, 8, 10).
"""

# Q61. Debug the Accumulator
"""
1. Identify the mistake: sum = i overwrites the accumulator instead of adding to it.
2. Correct the program:
sum = 0
for i in range(1, 6):
    sum = sum + i
print(sum)

3. Explanation: The accumulator sum needs to retain its previous value and add the new value of i to it in every iteration.
"""

# Q62. Daily Expense Analyzer
n = int(input("Enter number of days: "))
total = 0
highest = 0
lowest = float('inf')

for i in range(n):
    exp = int(input(f"Enter expense for day {i+1}: "))
    total += exp
    if exp > highest:
        highest = exp
    if exp < lowest:
        lowest = exp

print(f"Total: {total}\nHighest: {highest}\nLowest: {lowest}")

# Q63. Student Marks Analyzer
n = int(input("Enter number of subjects: "))
total = 0
highest = 0
lowest = float('inf')

for i in range(n):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = total / n
print(f"Total: {total}\nAverage: {average}\nHighest: {highest}\nLowest: {lowest}")

# Q64. Attendance Analyzer
n = int(input("Enter number of working days: "))
present = 0
absent = 0

for i in range(n):
    status = input("Enter status (P/A): ").upper()
    if status == 'P':
        present += 1
    elif status == 'A':
        absent += 1

attendance = (present / n) * 100
print(f"Present: {present}\nAbsent: {absent}\nAttendance: {attendance:.2f}%")

# Q65. Electricity Usage Analyzer
n = int(input("Enter number of days: "))
total_units = 0
days_above_10 = 0

for i in range(n):
    units = int(input(f"Enter units for day {i+1}: "))
    total_units += units
    if units > 10:
        days_above_10 += 1

print(f"Total Units: {total_units}\nDays Above 10: {days_above_10}")

# Q66. Shopping Bill Analyzer
n = int(input("Enter number of products: "))
total_bill = 0
above_1000 = 0

for i in range(n):
    price = int(input(f"Enter price for product {i+1}: "))
    total_bill += price
    if price > 1000:
        above_1000 += 1

print(f"Total Bill: {total_bill}\nProducts Above 1000: {above_1000}")

# Q67. Login Attempt Analyzer
n = int(input("Enter number of login attempts: "))
success = 0
failed = 0

for i in range(n):
    attempt = input("Enter attempt (success/failed): ").lower()
    if attempt == "success":
        success += 1
    elif attempt == "failed":
        failed += 1

success_rate = (success / n) * 100
print(f"Successful: {success}\nFailed: {failed}\nSuccess Rate: {success_rate}%")

# Q68. Number Profile
num = int(input("Enter a positive integer: "))
digit_count = int(math.log10(num)) + 1
total_sum = 0
largest = -1
smallest = 10
even_count = 0
odd_count = 0

for i in range(digit_count):
    digit = num % 10
    total_sum += digit
    
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
        
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    num = num // 10

print(f"Digits: {digit_count}\nSum: {total_sum}\nLargest: {largest}\nSmallest: {smallest}\nEven Digits: {even_count}\nOdd Digits: {odd_count}")

# Q69. String Balance Challenge
s = input("Enter a string: ")
total_chars = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index_chars = 0

for i in range(len(s)):
    total_chars += 1
    char = s[i]
    
    if i % 2 == 0:
        even_index_chars += 1
        
    if char != " ":
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
            
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1

print(f"Total Characters: {total_chars}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Even Index Characters: {even_index_chars}")

