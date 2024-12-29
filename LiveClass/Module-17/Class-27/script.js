/* JavaScript Object */
let car = {
    /* key/property: value */
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
    /* key/property: value */
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

/* JavaScript Array */
let teams = ["Real Madrid", "Barcelona", "Manchester United", "Bayern Munich"];
let teamsToUpper = teams.map(team => team.toUpperCase());
let teamsAsc = teams.sort();
let teamsDesc = teams.reverse();

// teams.forEach(team => console.log(team));

/* JavaScript String */

let str = "Hello, World!";
let singleQuoteStr = 'Hello, World!';
let doubleQuoteStr = "Hello, World!";

// Template Literal
let fname = "Fahad";
let lname = "Chowdhury";
let templateStr = `Hello, ${fname} ${lname}`;

/* JavaScript String Operations */
let str1 = "Hello";
let str2 = "World";

let strConcat = str1 + " " + str2;
let strConcat2 = `${str1} ${str2}`;
let strRepeat = str1.repeat(3);
let strLength = str1.length;
let strSubstr = str1.substr(0, 3);
let strSlice = str1.slice(0, 3);
let strReplace = str1.replace("Hello", "Hi");
let strSearch = str1.search("l");
let strUpperCase = str1.toUpperCase();
let strLowerCase = str1.toLowerCase();
let strTrim = "   Hello   ".trim();
let strTrimLeft = "   Hello   ".trimLeft();
let strTrimRight = "   Hello   ".trimRight();
let strPadStart = "Hello".padStart(10, "0");
let strPadEnd = "Hello".padEnd(10, "0");
let strSplit = str1.split("");
let strCharAt = str1.charAt(0);
let strCharCodeAt = str1.charCodeAt(0);
let strIndex = str1.indexOf("l");
let strLastIndex = str1.lastIndexOf("l");
let strIncludes = str1.includes("l");
let strStartsWith = str1.startsWith("H");
let strEndsWith = str1.endsWith("o");
let strMatch = str1.match("l");
let strMatchAll = str1.matchAll("l");

/* JavaScript Date and Time */
let date = new Date();
let dateYear = date.getFullYear();
let dateMonth = date.getMonth();
let dateDay = date.getDate();
let dateHours = date.getHours();
let dateMinutes = date.getMinutes();
let dateSeconds = date.getSeconds();
let dateMilliseconds = date.getMilliseconds();
let dateTime = date.getTime();
let dateUTC = date.toUTCString();
let dateString = date.toString();
let dateLocaleString = date.toLocaleString();
let dateLocaleDateString = date.toLocaleDateString();
let dateLocaleTimeString = date.toLocaleTimeString();
let dateISO = date.toISOString();
let dateISOString = date.toISOString();
let dateJSON = date.toJSON();
let dateUTCString = date.toUTCString();

/* JavaScript Math */
let num = 10;
let numAbs = Math.abs(-10);
let numCeil = Math.ceil(10.1);
let numFloor = Math.floor(10.9);
let numRound = Math.round(10.5);
let numMax = Math.max(10, 20, 30, 40, 50);
let numMin = Math.min(10, 20, 30, 40, 50);
let numRandom = Math.random();
let numPow = Math.pow(2, 3);
let numSqrt = Math.sqrt(16);
let numSin = Math.sin(90);
let numCos = Math.cos(90);
let numTan = Math.tan(45);
let numLog = Math.log(10);
let numExp = Math.exp(10);
let numPI = Math.PI;
let numE = Math.E;

/* JavaScript Number */
let num1 = 10;
let num2 = 20;

let numAdd = num1 + num2;
let numSub = num1 - num2;
let numMul = num1 * num2;
let numDiv = num1 / num2;
let numMod = num1 % num2;
let numInc = num1++;
let numDec = num1--;
let numParseInt = parseInt("10");
let numParseFloat = parseFloat("10.5");
let numIsNaN = isNaN("Hello");
let numIsFinite = isFinite(10);
let numToFixed = num1.toFixed(2);
let numToString = num1.toString();
let numValueOf = num1.valueOf();
let numLocaleString = num1.toLocaleString();
let numToExponential = num1.toExponential();
let numToPrecision = num1.toPrecision(2);
let numIsInteger = Number.isInteger(num1);

/* JavaScript Window */
let windowWidth = window.innerWidth;
let windowHeight = window.innerHeight;
let windowLocation = window.location;
let windowNavigator = window.navigator;
let windowHistory = window.history;
let windowScreen = window.screen;
let windowDocument = window.document;
let windowOuterWidth = window.outerWidth;
let windowOuterHeight = window.outerHeight;
let windowScreenX = window.screenX;
let windowScreenY = window.screenY;
let windowScreenLeft = window.screenLeft;
let windowScreenTop = window.screenTop;
let windowScrollX = window.scrollX;
let windowScrollY = window.scrollY;

/*window.alert("Hello, World!");
window.confirm("Are you sure?");

var myName = window.prompt("Enter your name: ");
console.log(myName);

window.open("https://www.google.com", "_blank");

setInterval(
  () => console.log("Hello, World!"), 1000
);*/

console.log(navigator.appName);
console.log(navigator.appVersion);
console.log(navigator.userAgent);