// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]



const { melon_data: song_array, melon_data } = require("./melon_data");


const filter_song = song_array.filter(
    (song) => song.title.includes("사랑")
).map(
    ({ title }) => title
);

console.log(filter_song);
