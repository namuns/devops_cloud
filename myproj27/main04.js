// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`



const { melon_data: song_array, melon_data } = require("./melon_data");

const filter_song = song_array.sort(function (a, b) { return b.like - a.like }).filter((song) => (song.like >= 200000));

for (const song of filter_song) {
    console.log(song.like, song.title, song.artist);
}
