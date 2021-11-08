
#title_list: List[str] = []
from typing import List  # 타입힌팅(무슨 타입인지 알려줌 코딩 효율 향상)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""

title_list: List[str] = []

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist == "방탄소년단":
        title: str = song_dict["title"]
        title_list.append(title)

print(title_list)



"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""

title_list: List[str] = []

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist == "방탄소년단":
        title: str = song_dict["title"]
        title_list.append(title)

print(title_list)



"""
"좋아요" 수가 200,000 이상인 곡들의 곡명 리스트를 만들어보세요.
"""

title_list: List[str] = []

for song_dict in song_list:
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    if like >= 200_000:
        title_list.append(title)

print(title_list)
