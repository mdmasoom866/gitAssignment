# # ques 1
# num = 5 ;
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print("*", end=" ")
#     print()

# # ques 2
# num = 3;
# for i in range(1,num+1):
#     for j in range(1,7):
#         print("*" ,end=" ")
#     print()

# # ques 3
# num=5 
# for i in range(1,num+1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()

# # ques 4
# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # ques 5
# num = 5
# for i in range(1,num+1):
#     for j in range(0,i):
#         print(i, end=" ")
#     print()

# # ques 6
# num = 5
# for i in range(1,num+1):
#     for j in range(0,i):
#         print(chr(65+i), end=" ")
#     print()
    
# # ques 7
# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()    

# ques 8
# num= 5
# for i in range(1,num+1):
#     for j in range(0,i):
#         print(i+(j), end=" ")
#     print()     

# # ques 9
# num=5
# for i in range(1,num+1):
#     start=1
#     if i%2==0:
#         start=0
#     for j in range(1,i+1):
#         print(start ,end=" ")
#     print()  

# # ques 10
# num = 5
# for i in range(1,num+1):
#     for j in range(num+1,i,-1):
#         print("*", end=" ")
#     print()       

# # ques 11
# num = 5
# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(j,end=" ")
#     print()    

# # ques 12
# num = 5
# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(chr(64+j), end=" ")
#     print()    

# # ques 13
# num = 5
# for i in range(1,num+1):
#     for j in range(num-i,0,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*", end=" ")
#     print() 


# # ques 14
# num = 5
# for i in range(1,num+1):
#     for k in range(1,i):
#         print(" ", end=" ")
#     for j in range(num+1,i,-1):
#         print("*", end=" ")
#     print() 

# # ques 15
# num = 5
# for i in range(1,num+1):
#     for j in range(num,i,-1):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print("*", end=" ")
#     print()                              

# # ques 16
# num = 5
# for i in range(1,num+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for k in range(i*2,num*2+1):
#         print("*", end=" ")
#     print()


# # ques 17
# n = 5
# # Upper half (including the widest middle row)
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# # Lower half
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# # ques 18
# # Task: Print the pattern shown, adjusting its size based on the input.
# num = 5 ;
# for i in range(1,num+1):
#     for j in range(num-i,0,-1):
#         print(" ", end=" ")
#     for k in range(1,num):
#         print("*",end=" ")
#     print()        

# # ques 19
# #  Task: Print the pattern shown, adjusting its size based on the input.

# num = 5 ; 
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     for j in range(i,(num*2)-i):
#         print(" ", end=" ")
#     for k in range(i,0,-1):
#         print(k, end=" ")        
#     print()


# # ques 20
# # Task: Print the pattern shown, adjusting its size based on the input.
# num= 5;
# for i in range(1,num+1):
#     for j in range(num-i,0,-1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()    

# # ques 21
# num = 5
# for i in range(1,num+1):
#     for j in range(i,num):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")    
#     print()    


# # ques 22
# num = 5
# for i in range(1,num+1):
#     for j in range(i,num):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(chr(64+k),end=" ")
#     for l in range(i-1,0,-1):
#         print(chr(64+l),end=" ")    
#     print()   

# #ques 23
# num = 5
# for i in range(1,num+1):
#     for j in range(num+1,num+i):
#         print(chr(62+j),end=" ")
#     for k in range(0,1):
#         print(chr(69),end=" ")
#     print()

# # ques 24
# num = 5
# for i in range(1,num+1):
#     for j in range(0,i):
#         print("*",end=" ") 
#     print()  
# for a in range(1,num): 
#     for k in range(num,a,-1):
#         print("*",end=" ")
#     print()    


# # ques 25
# num = 8;
# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(j,end=" ")
#     print()
# for a in range(1,num):
#     for k in range(1,a+2):
#         print(k,end=" ")
#     print()    

# # ques 26
# num = 5 
# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(chr(64+j),end=" ")
#     print()
# for a in range(1,num):
#     for k in range(1,a+2):
#         print(chr(64+k),end=" ")
#     print() 


# # ques 27
# num = 5
# start1 = "#"
# start2 ="*"
# for i in range(1,num+1):
#     if i%2==0:
#         for j in range(1,num+1):
#             if j%2==0:
#                 print(start2,end="")
#             else:
#                 print(start1,end=" ")
#     else:
#         for k in range(1,num+1):
#             if k%2==0:
#                 print(start1,end=" ")
#             else:
#                 print(start2,end=" ")    
#     print()


# # ques 28
# num = 6
# start1 = "1"
# start2 ="0"
# for i in range(1,num+1):
#     if i%2==0:
#         for j in range(1,num+1):
#             if j%2==0:
#                 print(start2,end="")
#             else:
#                 print(start1,end=" ")
#     else:
#         for k in range(1,num+1):
#             if k%2==0:
#                 print(start1,end=" ")
#             else:
#                 print(start2,end=" ")    
#     print()


# # ques 29
# num =5 
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(i*j,end=" ")
#     print()


# # ques 30 
# num = 5
# for i in range(1,num+1):
#     if i%2==0:
#         for j in range(i,0,-1):
#             print(j,end=" ")
#     else:
#         for k in range(1,i+1):
#             print(k,end=" ")
#     print()


# # ques 31
# num = 4;
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for k in range(1,i):
#         print(reversed(k),end=" ")
#     print()
# for l in range()

# ques 32
