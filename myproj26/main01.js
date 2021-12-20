// var name = "남문수"; // 선언
// name = "steve"; // 변경


// 변수선언
let name = "남문수"; // 선언
name = "steve";  // 변경


// 상수(constant)선언(변경 거부 됨)
const age = 10;
// age = 12; // 상수는 값을 변경 할 수 없다.


console.log(name, age);

// 제어구조

const number = 10;

if (number % 2 === 0) {
    console.log("짝수");
}
else {
    console.log("홀수");
}



for (let i = 1; i < 11; i++) {
    console.log(i)
}

for (let i = 1; i < 11; i += 2) {
    console.log(i)
}

// 함수
function mysum(x, y) {
    return x + y;
}

// 익명함수
const mysum2 = function (x, y) {
    return x + y;
}
console.log(1, 2);

// arrow function
const mysum3 = (x, y) => {
    return x + y;
}
console.log(1, 2);

// 중괄호 안쓰면 바로 리턴 되는
const mysum4 = (x, y) => x + y;
console.log(mysum4(1, 2))


//
function mysum5(x, y, ...args) {
    console.log(x, y, args);
}
mysum5(1, 2, 3, 4, 5);


// 
function reducer(preValue, currentValue) {
    return preValue + currentValue;
}
const result = [1, 2, 3, 4, 5].reduce(reducer, 0);
console.log(result);


const result2 = [1, 2, 3, 4, 5].reduce((preValue, curruntValue) => {
    return preValue = curruntValue;
}, 0);
console.log(result2);



const result3 = [1, 2, 3, 4, 5].reduce(
    (preValue, curruntValue) => preValue = curruntValue,
    0);
console.log(result3);