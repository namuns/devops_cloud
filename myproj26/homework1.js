//셔플 돌리기
const shuffle = () => (Math.random() - 0.5);
const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];
const shuffled = [...animal_names].sort(shuffle);


// 시간재기
begin_time = Math.floor(+ new Date() / 1000);

let cor_counter = 0;

// 슬라이스
const random_name = shuffled.slice(0, 5);

for (i = 0; i < random_name.length; i++) {
    console.log(random_name[i]);
    const { question } = require("readline-sync");
    const name = question(">>> ")
    if (name == random_name[i]) {
        cor_counter += 1;
        console.log("정확합니다.")
    } else {
        console.log("오타입니다.")
    }
}

// 계산 및 메세지
end_time = Math.floor(+ new Date() / 1000);
now_time = end_time - begin_time
console.log(`${cor_counter}번 성공하셨습니다.`)
console.log(`총${now_time}초가 걸렸습니다.`)