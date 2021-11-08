from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 방탄소년단의 노래에 대해서만 곡명과 곡명의 글자수를 출력

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서 filter
# 각 곡의 좋아요 수와 제목글자수의 곱을 구해보세요


# 1) for/if로 구현

for song_dict in song_list:
    if len(song_dict["artist"]) >= 3:
        print(song_dict["like"] * len(song_dict["title"]))


#밑에꺼하고 같다


new_song_list: List[int] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value: int = song_dict["like"] * len(song_dict["artist"])

        new_song_list.append(dict(song_dict, value=value))

        # 밑에꺼하고 같다

        new_song_list.append(
            {
                "title": song_dict["title"],
                "artist": song_dict["artist"],
                "like": song_dict["like"],
                "rank": song_dict["rank"],
            }
        )

for song_dict in new_song_list:
    print("{title} / {value}".format(**song_dict))


# 2) filter / map


def get_artist_words(song_dict):
    artist: str = song_dict["artist"]
    like: int = song_dict["like"]
    return [artist, len(artist), like]


for title, length, like in map(get_artist_words, song_list):
    print(like * length)
