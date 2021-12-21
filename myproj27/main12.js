// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const { melon_data: song_array, melon_data } = require("./melon_data");


const countedArtist = song_array.reduce(function (allNames, song) {
    if (song.artist in allNames) {
        allNames[song.artist]++;
    }
    else {
        allNames[song.artist] = 1;
    }
    return allNames;
}, {});

const filtered_artist = Object.values(countedArtist).filter(
    (value) => (value > 1)
);

console.log(filtered_artist.length);