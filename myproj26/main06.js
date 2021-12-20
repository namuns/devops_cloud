
const tom = {
    name: "Tom",
    age: 10,
    region: "Daejeon",
}

// const name = tom.name;
// const age = tom["age"];

// const { name, age, region } = tom;
// console.log(name, age);


// 키 name을 읽어와서 otherName 변수에 저장
const { name: otherName } = tom;
console.log(otherName);


const steve = {
    name: {
        first: "Steve",
        last: "Jobs",
    },
    age: 10,
    region: "Daejeon",
};

const { name: otherName2 } = steve;
console.log(otherName);

const { name: { first } } = steve;
console.log(first);

const { name: { first: firstName } } = steve;
console.log(firstName);