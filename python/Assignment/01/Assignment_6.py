# ques 1
num = 5 ;
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*", end=" ")
    print()

# ques 2
num = 3;
for i in range(1,num+1):
    for j in range(1,7):
        print("*" ,end=" ")
    print()

# ques 3
num=5 
for i in range(1,num+1):
    for j in range(0,i):
        print("*", end=" ")
    print()

# ques 4
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# ques 5
num = 5
for i in range(1,num+1):
    for j in range(0,i):
        print(i, end=" ")
    print()

# ques 6
num = 5
for i in range(1,num+1):
    for j in range(0,i):
        print(chr(65+i), end=" ")
    print()
    
# ques 7
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()    

# ques 8
num= 5
for i in range(1,num+1):
    for j in range(0,i):
        print(i+j, end=" ")
    print()     

# ques 9
num=5
for i in range(1,num+1):
    start=1
    if i%2==0:
        start=0
    for j in range(1,i+1):
        print(start ,end=" ")
    print()        

