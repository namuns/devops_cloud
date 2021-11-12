import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# "좋아요수가 가장 많은 곡, 가장 작은 곡"

# 1번 songlist가 빈 리스트일 경우에 대한 대처
def peek_like_for_song(song_dict):
    return song_dict["like"]


song_dict = max(song_list, key=peek_like_for_song, default=None)
if song_dict == None:
    print("노래 목록이 비었습니다")
else:
    print(song_dict)
# 2번 songlist가 빈 리스트일 경우에 대한 대처

try:
    song_dict = max(song_list, key=peek_like_for_song)
except ValueError:

    print("노래 목록이 비었습니다")
else:
    print(song_dict)

# 3번 songlist가 빈 리스트일 경우에 대한 대처

if song_list:
    song_dict = max(song_list, key=peek_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다.")


# 곡명 단어수 가장 많은 곡, 가장 작은 곡"




# 곡명 글자수 가장 많은 곡, 가장 작은 곡"
