"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 리스트를 만들어서 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠
"""
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 곡명 단어수로 top10 곡명리스트를 만들어봅시다.


def pick_word_count_for_title(song_dict):
    # return song_dict("like")
    title: str = song_dict["title"]
    word_list = title.split()
    return len(word_list)


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in sorted_song_list[:10]:
    print("{like} {title}".format(**song_dict))
