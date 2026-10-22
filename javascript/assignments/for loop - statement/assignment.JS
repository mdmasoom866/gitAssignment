// LOOPING QUSESTION :-
// QUES 1
// A teacher wants students to practice counting. Write a program to print all numbers from 1 to 15.
for( i=1; i<=15; i++){
    console.log(i)
}

// ques 2
// A school has lockers numbered with even numbers for a special activity. Write a program to print all even numbers from 2 to 40.
for(i=2; i<=40; i+=2){
    console.log(i)
}

// ques 3
// A fitness coach assigns odd numbers to participants for a special activity. Write a program to print all odd numbers from 1 to 35.
for(i=1 ; i<=35 ; i+=1){
    if(i%2!=0){
        console.log(i)
    }
}

// ques 4
// You save ₹10 on Day 1, ₹20 on Day 2, ₹30 on Day 3, and continue increasing your daily savings by ₹10. Write a program to calculate your total savings after 10 days.
for(i=0 ; i<=100 ; i+=10){
    console.log(i)
}

// ques 5
// You want to practice multiplication. Write a program to print the multiplication table of 12, from 12 × 1 to 12 × 10.
for(i=1; i<=10; i++){
    console.log(`12*${i} = (12*${i}`)
}

// ques 6
// You drink 3 glasses of water every day. Write a program to calculate the total number of glasses you drink over 7 days. Print the cumulative total after each day.

let glasses = 0;
for(i=1; i<=7; i++){
    glasses+=3
    console.log(`day ${i} : ${glasses}`)
}

// ques 7
// One chocolate costs ₹15. Write a program to print the total cost of buying 1 to 10 chocolates.
let amount = 15;
for(i=1; 1<=10; i++){
    console.log(`${i} choclate = ${amount}`);
    amount+=15;
}

// ques 8
// You want to calculate the sum of all even numbers between 2 and 30, including both 2 and 30. Write a program to calculate and print the total.
let sum = 0;
for(i=2 ; i<=30 ; i+=2){
    sum+=1;
    console.log(`sum of all even numbers ${sum}`)
}

// ques 9
// You do 5 push-ups on Day 1, 10 on Day 2, 15 on Day 3, and continue increasing the number by 5 each day. Write a program to print the number of push-ups for each day over 7 days.
let pushUp = 5;
for(i=1; i<=7; i++){
    pushUp+=5
    console.log(`day ${i} = ${pushUp} push-ups`)
}

// ques 10
// One movie ticket costs ₹150. Write a program to print the total ticket cost for 1 to 8 people.
ticket = 150;
for(i=1; i<=8; i++){
    console.log(`${i} Person : ${ticket}`)
    ticket+=150;
}


//  part -B ] for loop (additional advance questions)

//  Given an array of temperatures [28, 32, 25, 40, 18, 35], use a for loop to count how many days were hotter than 30°C.
// let arr = [28,32,25,40,18,35];
// let count = 0;
// for(i=0; i<=arr.length-1; i++ ){
//     if(arr[i]>30){
//         count+=1;
//     }
// }console.log(count)

// Write a for loop that calculates the sum of all digits of a given number (example: 4729 → 4+7+2+9 = 22).
// let num = "4729";
// let summ = 0
// for(i=0; i<=num.length-1; i++){
//     summ+=Number(num[i]);
// }console.log(summ)

// Create a for loop that prints only the numbers between 1 and 100 that are divisible by both 3 and 5, but not by 7.
// for(i=1; i<=100; i++){
//     if(i%3==0 && i%5==0 && i%7!=0){
//         console.log(i)
//     }
// }

// Given the string "JavaScript", use a for loop to create a new string that contains only the consonants (remove vowels).
// let str = "javascript" ;
// let newString = "" ;
// for(i=0; i<=str.length[i]; i++){
//     if(str[i]!="a" && str[i]!="e" && str[i]!="i"&& str[i]!="o"&&str[i]!="u"){
//         newString += str[i]
//     }
//    console.log(newString)
// }

// Write a for loop that finds the largest number in an array of positive integers without using any sorting method.

let arr = [10,20,30,40];
for(i=0; i<=arr.length-1; i++){
    if(arr[0]>arr[1] && arr[0]>arr[2] && arr[0]>arr[3]){
        console.log(arr[0])
    }else if(arr[1]>arr[0] && arr[1]>arr[2] && arr[1]>arr[3]){
        console.log(arrp[1])}
    else if(arr[2]>arr[1] && arr[2]>arr[0] && arr[2]>arr[3]){
        console.log(arrp[2]) }
    else(arr[3]>arr[1] && arr[3]>arr[2] && arr[3]>arr[0])
        {console.log(arr[3])}
    }

// Use a for loop to check whether a given number is a perfect number (a number equal to the sum of its proper divisors). Example: 28.





// Print the following series using a single for loop:
// 1 2 4 8 16 32 64 128
// num = 1
// for(i=1; i<=128; i*=2){
//     console.log(i);
    
// }   


// 
