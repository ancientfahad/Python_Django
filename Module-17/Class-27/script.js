/*
    JavaScript Object
*/

let car = {
    //** key/property: value **//
    brand: "Toyota",
    model: "Corolla",
    year: 2022,
    features: ["AC", "Bluetooth", "Touch Screen Panel", "GPS"],
    start: function() {
        console.log("The car is starting...");
    },
    stop: function() {
        console.log("The car is stopping...");
    }
}

let carJSON = {
    //** key/property: value **//
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "features": ["AC", "Bluetooth", "Touch Screen Panel", "GPS"],
    "start": function() {
        console.log("The car is starting...");
    },
    "stop": function() {
        console.log("The car is stopping...");
    }
}

let carJSONString = JSON.stringify(car);
let carObj = JSON.parse(JSON.stringify(carJSON));

// console.log(`Car: ${car}`);
// console.log(`Car JSON String: ${carJSONString}`);
// console.log(`Car Obj: ${carObj}`);

// console.log(car.brand);
// console.log(car.features[0]);
// car.start()
// car.stop()

/*
    JavaScript Array
*/

let teams = ["Real Madrid", "Barcelona", "Manchester United", "Bayern Munich"];
let teamsToUpper = teams.map(team => team.toUpperCase());
let teamsAsc = teams.sort();
let teamsDesc = teams.reverse();

// teams.forEach(team => console.log(team));

/*
    JavaScript String
*/

let str = "Hello, World!";
let singleQuoteStr = 'Hello, World!';
let doubleQuoteStr = "Hello, World!";

// Template Literal
let fname = "Fahad";
let lname = "Chowdhury";
let templateStr = `Hello, ${fname} ${lname}`;