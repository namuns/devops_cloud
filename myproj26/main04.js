
// 객체 복사 키값은 항상 쌍따옴표

const obj1 = { "value1": 10, "p-1": 20, };

obj1["value1"]
obj1.value1 // 둘이 같다.

obj1["p-1"]
obj1.p - 1 // 이건안됨


console.log(obj1.name); // 이거 undefined 나옴(지정속성이 없어서)

// js에서는 함수가 아무런 값도 리턴하지 않으면 undefined 반환
function fn() { }
console.log(fn());





// 객체 복사
const obj1 = { "value1": 10 };
const obj2 = obj1; // 얕은 복사(같은 값)가 됨


// 깊은복사는 기존값 + 인스턴스까지
// 아래는 많은 깊은 복사 방법 중의 무식한 하나
const json_string = JSON.stringify(obj1)
const obj3 = JSON.parse(json_string);

obj1.value1 += 1;

console.log(obj1);
console.log(obj2);
console.log(obj3);

