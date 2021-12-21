const { melon_data: song_array, melon_data } = require("./melon_data");


for (const song of song_array) {
    song_array.sort(function (a, b) { return b.like - a.like });
    console.log(song.like, song.title);
}

