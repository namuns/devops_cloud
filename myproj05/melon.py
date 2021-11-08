# 기초 데이터로서 멜론 top100 리스트 구성하기

from typing import Counter
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

#

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])


###


for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])


#####

song_count = 0
for song_dict in song_list:
    if song_dict["like"] > 200_000:
        song_count += 1
print(f"좋아요가 20만 넘는 곡은 {song_count}곡입니다.")


#########################
#######가수 별 곡수#######
#########################

artist_dict = {}
for song_dict in song_list:
    artist: str = song_dict["artist"]

    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

print(artist_dict)


# list comprehension 문법이다.
artist_list = [song_dict["artist"] for song_dict in song_list]

print(Counter(artist_list))
