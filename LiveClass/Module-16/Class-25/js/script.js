/* Primitive Types */
var name = 'John'; // String Literal
var age = 30; // Number Literal
var isApproved = true; // Boolean Literal
var firstName = undefined;
var selectedColor = null;

/* Reference Types */
var numbers = [1, 2, 3, 4, 5]; // Array
var person = {
    name: 'John',
    age: 30
}; // Object

console.log(person);
console.log(typeof person);
console.log(typeof numbers);

document.write(person);
document.write("<br>");
document.write(typeof person);

/* Conditional Statements */
/* If-Else */

var hour = 10;

if (hour > 10) {
    console.log('It is after 10');
} else {
    console.log('It is before 10');
}

/* Switch-Case */
var role = 'guest';
switch (role) {
    case 'admin':
        console.log('Admin User');
        break;
    case 'guest':
        console.log('Guest User');
        break;
    default:
        console.log('Unknown User');
}

/* Loops */
/* For Loop */
for (var i = 0; i < 5; i++) {
    console.log('Hello World');
}

/* While Loop */
var i = 0;
while (i < 5) {
    console.log('Hello World');
    i++;
}
/* Do-While Loop */
var j = 0;
do {
    console.log('Hello World');
    j++;
}
while (j < 5);
/* For-Each Loop */
var colors = ['red', 'green', 'blue'];
for (var color of colors) {
    console.log(color);
}
/* For-In Loop */
var person = {
    name: 'John',
    age: 30
};
for (var key in person) {
    console.log(key, person[key]);
}
/* For-Of Loop */
var colors = ['red', 'green', 'blue'];
for (var index in colors) {
    console.log(index, colors[index]);
}