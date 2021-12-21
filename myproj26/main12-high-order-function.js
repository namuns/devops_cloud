
// function base_10(fn) {
//     function wrap(x, y) {
//         return fn(x, y) + 10;
//     }
//     return wrap;
// }


// function mysum(x, y) {
//     return x + y;
// }

// base_10(base_10(base_10(mysum)));

// console.log(mysum(1, 2))


// arrow


const base_10 = (fn) => (x, y) => fn(x, y) + 10;



let mysum = (x, y) => x + y;

mysum = base_10(base_10(base_10(mysum)));

console.log(mysum(1, 2))