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



