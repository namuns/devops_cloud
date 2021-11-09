"""
리스트에 랭크된 가수는 총 몇 팀인가요?(중복 제거한 가수명 리스트의 크기)
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 가수명 뽑아서 중복제거

# 1번 방법

artist_list = []

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)
print(len(artist_list))


# 2번 방법(집합사용)
# 리스트 소괄호 빈 집합이만들어짐
# add 매서드

artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
print(len(artist_set))


# 3번 방법
# 리스트를 먼저 만든 후 집합으로 변환
# 같다 for song_dict in song_list
#           song_dict["artist"]

artist_set = set([song_dict["artist"] for song_dict in song_list])
print(len(artist_set))


# 4번 방법
# 그대로 복사 set 지움
# 대괄호를 중괄호로
# set comprthension 중복을 알아서 배제해줌

artist_set = {song_dict["artist"] for song_dict in song_list}
print(len(artist_set))
