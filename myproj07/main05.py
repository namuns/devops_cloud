"""2곡 이상 랭크된 가수는 총 몇 팀?"""

from collections import defaultdict, Counter
from pprint import pp, pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 어떤 가수가 각 몇곡이 있는지 찾는다.
# counter 써도됨

artist_list = [song_dict["artist"] for song_dict in song_list]

# 1번 방법
song_count_dict = {}  # key = artist, value : song count
for artist in artist_list:
    if artist not in song_count_dict:
        song_count_dict["artist"] = 0
    song_count_dict["artist"] += 1

###
pprint(song_count_dict)


# 2번 방법
# 키에러가 발생할 떄 키에러를 숨기고
# 지정된 디폴트 값으로 key/value 를 지정합니다


song_count_dict = defaultdict(int)  # key = artist, value : song count
for artist in artist_list:
    song_count_dict[artist] += 1

pprint(song_count_dict)


# 3번 방법
song_count_dict = Counter(artist_list)

# 1
artist_count_above_2 = 0
for song_count in song_count_dict.values():
    if song_count >= 2:
        artist_count_above_2 += 1
pprint(artist_count_above_2)

# 2


def check_above_1(song_count):
    return song_count > 1


print(len(list(filter(check_above_1, song_count_dict.values()))))
