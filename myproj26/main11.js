const fs = require("fs");

// 1번 콜백
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// })

// 2번 Promise
// const fsPromises = fs.promises;

// fsPromises.readdir("c:/Dev")
//     .then(files => console.log("loaded :", files))
//     .catch(error => console.error(error));
// console.log("ENDED");



// 3번

const fsPromises = fs.promises;

// await는 promise 문법에 대한 축약 async 필수
async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loaded :", files);
    }
    catch (error) {
        console.error(error);
    }
}
main();

