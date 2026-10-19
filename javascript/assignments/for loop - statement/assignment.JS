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

