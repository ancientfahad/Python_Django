/* Named Function */
function myFunction() {
    console.log('Hello World!');
}

myFunction();

function sumOfTwoNumbers(a, b) {
    let c = a + b;
    return c;
}

console.log(`Sum of two numbers: ${sumOfTwoNumbers(10, 20)}`);

function subOfTwoNumbers(a, b) {
    let c = a - b;
    return c;
}

console.log(`Subtraction of two numbers: ${subOfTwoNumbers(50, 40)}`);

function multiplyOfTwoNumbers(a, b) {
    let c = a * b;
    return c;
}

console.log(`Multiplication of two numbers: ${multiplyOfTwoNumbers(5, 6)}`);

function divisionOfTwoNumbers(a, b) {
    let c = a / b;
    return c;
}

console.log(`Division of two numbers: ${divisionOfTwoNumbers(100, 10)}`);

function greet(name) {
    return `Hello ${name}!`;
}

console.log(greet('John Doe'));

/* Anonymous Function */
anonymousFunction = function(a, b){
    return a * b;
}

console.log(anonymousFunction(10, 20));

/* Arrow Function */
const arrowFunction = (a, b) =>  a * b;
console.log(arrowFunction(5, 6));

/* Callback Function */
/* IIFE */
(function autoWelcome() {
    console.log('Welcome to my page!');
})();

const appConfig = (function() {
    const apiKey = "123456";
    return {apiKey};
})();

console.log(appConfig);
console.log(appConfig.apiKey);

/* Generator Function */
function* generatorFunction(){
    yield 'Hello';
    yield 'World';
    yield 'Done';
    return 'Bye';
}

const gen = generatorFunction();

console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

/* Recursive Function */
/* Factorial */

// 5! = 5 * 4 * 3 * 2 * 1 = 120

function factorial(n) {
    if(n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

console.log(factorial(5));

function factorialLoop(n) {
    let result = 1;
    for(let i = 1; i <= n; i++) {
        result *= i;

        console.log(`i: ${i}, result: ${result}`);
    }
    return result;
}

console.log(factorialLoop(5));