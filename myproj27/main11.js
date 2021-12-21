// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set


const { melon_data: song_array, melon_data } = require("./melon_data");


let song_set = new Set();

for (const song of song_array) {
    song_set.add(song.artist);
}

console.log(song_set.size);