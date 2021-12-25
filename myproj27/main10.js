// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce


const { melon_data: song_array, melon_data } = require("./melon_data");

const filter_song = song_array.filter(
    (song) => (song.artist === "방탄소년단")
)
    .reduce(
        (accumulator, currentValue) => (accumulator + currentValue.like), 0
    );

console.log(filter_song);





Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
};

const result = song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"
    )
    .map(({ like }) => like)
    .sum();

console.log("result :", result);