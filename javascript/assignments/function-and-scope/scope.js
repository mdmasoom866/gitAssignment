// section 1 ( what is scope )
// QUES 1
var city = "Surat";
function display() {
    var country = "India";
    console.log(city);
    console.log(country);
}
display();
// Ques -1 
// => city  variable is displayed in global scope .
// ques -2
// => countryvariable is declared inside the funtion .
// ques -3
// => yes both teh variables can be accessed in the funstion display()  

// QUES 2 
var price = 500;
function calculate() {
    var tax = 50;
    console.log(price + tax);
}
calculate();
console.log(price);

// => 550 
// => 500


// QUES 3
var college = "ABC College";
function student() {
    var name = "Rahul";
    var age = 20;
}
function teacher() {
    var subject = "JavaScript";
}

// identif the scope of "college", "name", "age", and "subject"
//  -> college is a global scope 
//  -> name is a functional scope 
//  -> age is a funtional scope 
//  -> subject is a funtional scope 

// QUES 4
function first() {
    var number = 100;
}
function second() {
    console.log(number);
}
first();
second(); 
// what will happen when this code will execute ?
// -> when this code will execute from function first it will do nothing because there is no code to print the number .
// while this is come to second function then it will shoe the referenceerrorr that number is not defined .

// QUES 5 
// Write a JavaScript program that:

// Declares one variable in the global scope.
// Declares another variable inside a function.
// Prints both variables inside the function.
// Prints the global variable outside the function.

var name = "shah" ;
function greek(){
    var adddress = "jahrkhand"
    console.log(name)
    console.log(adddress)
}
greek();
console.log(name);


// section 2 : global scope 5 questions 
// QUES 6
var game = "Cricket";
function play() {
    console.log("I like " + game);
}
play();
console.log(game);
//  predict the out put of the code .
// -> i like cricket
// -> cricket 

// QUES 7
var language = "English";
function showLanguage() {
    console.log(language);
}
function changeLanguage() {
    language = "Gujarati";
    console.log(language)
}
showLanguage();
changeLanguage();
showLanguage();
console.log(language);

//  explain why the output is changing
// the output is change because the language english is in global scope and tehn the languages given is in the function so wo know that the functioin only takes teh value in the funtional scope . 

// QUES 8 

function displayMarks() {
    var marks = 75;
    console.log(marks);
}
displayMarks();


//  QUES 9 
// find the error in the code and predict the errorr 

var color = "Red";
function showColor() {
    var message = "Favorite color: ";
    console.log(message + color);
}
showColor();
console.log(color);


//  the error in the code is the sode of printing a message out side the funtion because we knoe that the teh varible message is a funtion scope so it can print only in the funtion .. 

//  and the out put of the code is favouriter color : red 
// red 

//  QUES 10 
// Write a program that declares a global variable named "school" with the value "Sunrise School".

// Create two functions:

// "showSchool()" should print the school name.
// "updateSchool()" should change the global variable to "Green Valley School".
// Call both functions in an appropriate order and print the final value of "school".
var school = "green valley school  "
function showschol(){
    var schoolName = "rmls";
    console.log(schoolName)
}
showschol();
function updateSchool(){
    console.log(school)
}
updateSchool();


//  SECTION 3 : FNCTION SCOPE 
// QUEW 11 
function calculateTotal() {
    var first = 100;
    var second = 200;
    console.log(first + second);
}
calculateTotal();
console.log(first);
