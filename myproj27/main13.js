// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.


const filter_song = song_array.filter(
    (song) => (song.artist === "방탄소년단")
).reduce(
    function (accumulator, currentValue) {
        if (!accumulator || currentValue.like > accumulator.like) {
            return currentValue;
        }
        else {
            return accumulator;
        }
    }, null
);

console.log(filter_song.title)