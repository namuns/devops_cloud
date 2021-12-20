

// 객체
const age1 = "나이";
const tom = {
    "name": "Tom",
    // "age": 10,
    // age: 10,
    [age1]: 10,

}

console.log(tom);


const name = "Tom";
const age = 10;
const tom1 = {
    name,
    age,
    print: function () {
        // console.log(this.name, this.age);
        // Template Literals라고한다. 줄바꿈은 그냥 엔터
        console.log(`안녕, 나는 ${this.name}이야. ${this.age}살이지.`);
    }
}

tom1.print();