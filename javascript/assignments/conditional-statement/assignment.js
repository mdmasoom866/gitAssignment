// // question 01

// let num = 25
// if (num%5==0){
//     console.log("yes,num is divisible by 5")
// }


// // question 02 

// let age  = 69 
// if (age >=60){
//     console.log("senior citizen")
// }


// // question 03 

// let num_1 = 200
// if (num_1>100){
//     console.log("yes ,it is a big no")
// }


// // question 04 

// let temp = 9 
// if ( temp<10){
//     console.log("very cold")
// }


// // question 05 

// let studentMarks = 100
// if(studentMarks==100){
//     console.log("perfect score")
// }


// // question 06

// let num_3= -2
// if(num_3<0){
//     console.log("Negative no ")
// }


// // question 07 


// let user = ""
// if(user==""){
//     console.log("empty string")
// }


// // question 08 
// let year  = 2000
// if ( year%100==0){
//     console.log("century year")
// }

// // question  09 

// let num_2 = 9 
// if (num_2>=0 && num_2%2==0){
//     console.log("Positive Even No")
// }


// // question 10 


// let marks  = 45
// if (marks>=35 && marks<=100){
//     console.log( "Valid marks ")
// }
// // PART-B

// // question 01 

// let num = 22
// if(num%2==0){
//     console.log("even")
// }
// else{
//     console.log("odd")
// }

// // question 02 

// let age  = 18 
// if(age>=18){
//     console.log("Eligible")
// }
// else{
//     console.log("not Eligible")
// }

// // question 03

// let num_1= 2
// if(num_1>=0){
//     console.log("positive")
// }
// else{
//     console.log("negative")
// }

// // question 04


// let marks  = 45
// if (marks>=35){
//     console.log("pass")
// }
// else{
//     console.log("fail")
// }

// // question 05

// let char = "Y"
// if(char>="A" && char<="Z"){
//     console.log("upper case letter")
// }else{
//     console.log("not a upper case character")
// }

// // question 06 

// let num_3 = 9 
// if(num%3==0){
//     console.log("no is divisible by 3")
// }
// else{
//     console.log("not divisible by 3")
// }


// // question 07 


// let year  = 2026
// if(year%4==0){
//     console.log("leap year")
// }
// else{
//     console.log("not a leap year ")
// }


// // question 08 

// let password = "admin123"
// if(password=="admin123"){
//     console.log("login successful")
// }
// else{
//     console.log("please tyr again")
// }


// // question 09

// let num_4 = 55
// let num_5 = 99
// if(num_4>num_5){
//     console.log("num_4 greater no")
// }
// else if (num_5>num_5){
//     console.log("num_5 is greater no ")
// }
// else{
//     console.log("both are equal ")
// }


// // question 10 

// let num_6 = 9
// if(num>0){
//     console.log("postive")
// }else if (num=0){
//     console.log("zero")
// }
// else{
//     console.log("negative")
// }

// SWITCH STATEMENTS

// ques 1
// Write a program that takes a month number (1–12) and prints the number of days in that month using switch
// let month = 4;
// switch(month){
//     case 1:
//         console.log("31 days")
//         break;
//     case 2:
//         console.log("28 days")
//         break;
//     case 3:
//         console.log("30 days")
//         break;
//     case 4:
//         console.log("31 days")
//         break;
//     case 5:
//         console.log("30 days")
//         break;
//     case 6:
//         console.log("31 days")
//         break;
//     case 7:
//         console.log("30 days")
//         break;
//     case 8:
//         console.log("31 days")
//         break;
//     case 9:
//         console.log("30 days")
//         break;
//     case 10:
//         console.log("31 days")
//         break;
//     case 11:
//         console.log("30 days")
//         break;
//     case 12:
//         console.log("31 days")
//         break;
//     default:
//         console.log("invalid month" )
// }

// ques 2
// Write a program that checks a character and prints whether it is a vowel or consonant using switch.
// variable = r;
// switch(variable){
//     case variable==a || variable==e || variable==i || variable==o || variable==u:
//         console.log("vowel");
//         break;
//     default:
//         console.log("consonent")    
// }


// ques 3
let num = 3;
switch(num){
    case num==1 || num==2:
        console.log("Winter")
        break;
    case num==3 || num==4:
        console.log("summer")
        break;
    default:
        console.log("invalid number")           
}

// ques 4
// Write a program using switch (true) to assign class based on marks:
// ≥ 75 → Distinction
// ≥ 60 → 1st class
// ≥ 50 → 2nd class
// ≥ 35 → 3rd class
// below 35 → Failed

// let marks = 93;
// switch(true){
//     case (marks>=75 || marks<=100):
//         console.log("Distinction")
//         break;
//     case (marks>=60 || marks<75):
//         console.log("1st class")
//         break;
//     case (marks>=50 || marks<60):
//         console/log("2nd class")  
//         break;
//     case (marks>=35 || marks<50):
//         console.log("3rd class")
//         break;
//     case (marks<35 || marks>=0):
//         console.log("fail")
//         break;
//     default:
//         console.log("invaild marks!")    

// }


// ques 5
// Create a nested switch program:
// First take a role (“admin” or “user”).
// If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.
// If role is “user”, print “Limited Access”.
// let role = admin ;
// switch(role){
//     case admin :
//         console.log("you can create edit and delete ")
//         break;
//     case user :
//         console.log("you have limited access") 
//         break;
//     default:
//         console.log("enter a valid occupation !")
// }

// ques 6
// Predict and explain the output of the following code. Then correct it so that only one message is printed:
// let fruit = "mango";
// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");
// }
// there is a variable friut and switch case is used to check the color of fruits . 

// ques 7
// Write a program that takes a value which can be either a number or a string (0, "0", false, null, undefined) and uses switch to correctly identify each one. Explain why some values may not match as expected.
// variable = null ;
// switch(variable){
//     case 0:
//         console.log(typeof(variable))
//         break;
//     case "0":
//         console.log(typeof(variable))
//         break;
//     case false:
//         console.log(typeof(variable))
//         break;
//     case null:
//         console.log(typeof(variable))
//         break;
//     case undefined:
//         console.log(typeof(variable))
//         break;    
//     default:
//         console.log("Invalid variable !")    
// }

// ques 8
// Create a tricky calculator using switch that supports these operations:
// +, -, *, /, %, and also ** (exponentiation).
// Handle division by zero properly inside the corresponding case.




// ternary operator 
// Write a ternary operator to check whether a given number is divisible by 7. If yes, return "Divisible by 7", otherwise "Not Divisible by 7".
