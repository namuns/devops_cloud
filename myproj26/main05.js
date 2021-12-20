
// Array
["Tom", 10, "Seoul"];

// 좌항 우항 개수 맞추지 않아도 된다.
// const [name] = ["Tom", 10, "Seoul"];

// 변수명 안써도 허용됨
// const [, age] = ["Tom", 10, "Seoul"];

// height는 undefined로 반환된다.
const [name, age, region, height] = ["Tom", 10, "Seoul"];

// 값 할당에 실패했을 때, 적용되는 피폴드값
const [name, age, region, height = 140] = ["Tom", 10, "Seoul"];

// 디폴트 값을 함수 호출로 지정 : 디폴트 값이 필요한 시점에 함수가 호출됩니다.
function get_default_height() {
    console.log("get_default_height 함수를 호출했습니다.");
    return 140;
}
// const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul", 150];

const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul", 150];

