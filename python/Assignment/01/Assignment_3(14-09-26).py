# ques ->1
a = 15
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

#ques ->2

x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)

# ques ->3

a = 10
b = 5

print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)

#ques ->4

print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")

#ques ->5

x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x)

#ques -> 6

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)

#ques ->7

marks = 50
print(marks>10)
print(marks<5)
print(marks*2)

# ques ->8
word = "computer"
print("p" in word)
print("x" in word)
print("c" not in word)

#ques ->9
text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)
# here the result are different because in print the first one "p" is started with capital and second one print  started with small p but the text python is started with samll p so the reult are diffent one is true and other is false . same thing is happen with the second one print .

# ques ->12
print(ord('A'))
print(ord('a'))
print(ord('Z'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
print(ord('@'))

#ques ->13
print(chr('65'))
print(chr('66'))
print(chr('97'))
print(chr('98'))
print(chr('48'))
print(chr('57'))
print(chr('64'))

#ques ->14
print(ord('A'))
print(ord('a'))
print(ord('B'))
print(ord('b'))
# ord of A is smaller then the ord value of a ...

#ques ->15
letter=input("ENter a character :")
print(ord('letter'))

#ques -17
letter = input("enter letter: ")
next_letter = ord(letter)+ 1
next_letter = chr(next_letter)
print("next letter", next_letter)



# question - 17

print("A" < "B")
#output - ture
print("a" < "b")
#output - Ture
print("A" < "a")
#output - True
print("0" < "9")
#output - True

#question - 18

print(chr(9731))
print(chr(9829))
print(chr(8377))

text = "PYTHON"
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])


#question - 20 

text = "COMPUTER"
print(text[0])
print(text[3])
print(text[-1])
print(text[-3])


#question -21

text = "PYTHON"

print(text[0])
#output - P
print(text[2])
#output - T
print(text[-1])
#output - N
print(text[-2])
#output - O


#question - 22


word = input("enter word: ")
print(word[1],"and",word[-1])


#question - 23

word = "PROGRAM"
word[0]
#P
word[2]
#O
word[-1]
#M
word[-4]
#G


text = "PYTHON"
print(text[0:3])
#output - PYT
print(text[2:5])
#output - THO
print(text[1:6])
#output - YTHON


#question - 25

text = "PROGRAMMING"

print(text[:4])
#PROG
print(text[4:])
#RAMMING
print(text[:])
#PROGRAMMING


#question  - 27

text = "PYTHON"


print(text[::2])
#output - PTO
print(text[1::2])
#output - YHN
print(text[::-1])
#output - NOHTYP


#question - 28 
string =input("enter string :")
print("reverse:",string[::-1])


#question - 29
string = input("enter string: ")
print(string[::2])


#question - 30
string = input("enter string: ")
print("first three letter:",string[:3])
print("last three characters:",string[-3:])


text = "ABCDEFGHIJ"
print(text[2:8:2])

print(text[8:2:-2])
print(text[::-2])

# start             stop              step
# 2                 8                 2
# 8                 2                 -2
# 0                 -1                -2  

text = "BTECH-CSE-2026"
print(text[:5])
print(text[6:9])
print(text[10:])
text = "Python is easy"

print(text.split())
#["Python","is","easy"]

#question - 34

data = "apple,banana,mango"

print(data.split(","))

# ['apple', 'banana', 'mango']


#question - 35

text = "Python is easy"

print(text.split(","))
#['Python is easy']

#question - 36

name,middle_name,surname = "Rahul Kumaar Sharma".split()
print(name)
print(middle_name)
print(surname)


#question - 37

first_name,last_name="Rahul Kumar".split()
print("fisrt_name:",first_name)
print("last_name: ",last_name)


#question - 38
num_1,num_2,num_3=input("enter no: ").split()
add = int(num_1)+int(num_2)+int(num_3)
print(add)

#question - 39

name,age,course,city="Rahul,20,BTech,Ahmedabad".split(",")
print("Name:",name)
print("Age:",age)
print("Course:",course)
print("City:",city)

#question - 40

username,domain=input("enter email").split()
print("Username:",username)
print("Domain:",domain)


#Question - 41

first,second,third,last=input("enter sentence").split()
print("first word",first)
print("Last word",last)
print("\nhello\nworld")


#question - 43

print("Name:\tRahul")
print("Age:\t20")
print("City:\tAhmedabad")

#question - 44
print("c:\\Python\\Programs")

#question - 45
print('it\'s Python')

#question - 46
print('he said \"hello"')

#question - 47
print("\nStudent Details\n")
print("\nName:\tRahul\nAge:\t20\nCourse:\tB.Tech")

#question - 49
print("2026", "09", "09", sep="-")
#2026-09-09

#question - 50
print("Hello", end=" ")
print("Python")
#Hello Python

#question - 51
print("10","20","30",sep="-" ,end="")
print("40","50","60",sep="-" )

#Quesstion - 52
name,age,city,cousre = input("enter details:").split()
print(f"\nName:{name}\nAge:{int(age)}\nCity:{city}\nCourse:{cousre}")


#question - 53

price = float(input("enter price:"))
print=(f"{price:.2f}")


#question - 54
age = input("Enter age: ")
print("Age after 5 years:", int(age) + 5)

#question - 55
print('It\'s Python')

#question - 56
text = "Python"
print(text[1:4])

#question - 57
a,b = input().split()

#Question - 58
a, b = input().split()

print(int(a )+ int(b))

#Question - 59

print("C:\\new\\test")

#question - 60 
name = input("enter name:")
physics = int(input("enter physics marks:"))
maths = int(input("enter maths marks:"))
python = int(input("enter python marks:"))

total = physics+maths+python
average = total/3
print("Name:",name)
print("Total:",total)
print("Average:",average)


#Question - 61
ID = input("enter id:").split()
Degree,Batch,Branch,Roll_number=ID
print(f"\nDegree:{Degree}\nBatch:{Batch}\nBranch:{Branch}\nRoll Number:{int(Roll_number)}")


#question - 62
full_name = input()
words = full_name.split()
username = words[0].lower() + "." + words[2].lower()
print(username)


#question - 63

take = "Python is very powerful".split()
first,second,third,last=take
print("first word:",first)
print("last word:",last)
print(take[:6])
print(take[-8:])

#Question - 64

email = input()


at_present = "@" in email
print(f"@ Present: {at_present}")


parts = email.split("@")
print(f"Username: {parts[0]}")
print(f"Domain: {parts[1]}")

#question - 65
char = input()
code = ord(char)
print(f"Character: {char}")
print(f"Code: {code}")
print(f"Previous: {chr(code - 1)}")
print(f"Next: {chr(code + 1)}")


#question - 66
product_name = input()
price = float(input())
quantity = int(input())
discount_percentage = float(input())

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


#question - 67


date_str = "09-09-2026"


day, month, year = date_str.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")


extracted_year = date_str[6:]
print(extracted_year)

#question - 68


text = "Python Programming"

words = text.split()
first_word = words[0]
second_word = words[1]


print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")

first_word_rev = first_word[::-1]
second_word_rev = second_word[::-1]


print(f"First Word Reversed: {first_word_rev}")
print(f"Second Word Reversed: {second_word_rev}")


#Question - 69


student_id = "BTECH-2026-CSE-105"


parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]


print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")

code = f"{degree[:]}/{branch[:]}/{roll[:]}"
print(f"Code: {code}")


#Question - 70


full_name = input("Enter full name: ")

words = full_name.split()


first_name = words[0]
last_name = words[-1]


first_upper_part = first_name[:3].upper()
last_lower_part = last_name[1:4]

reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper_part}")
print(f"Last Name (Lower Part): {last_lower_part}")
print(f"Full Name Reversed: {reversed_name}")
